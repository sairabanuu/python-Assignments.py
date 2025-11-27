import tkinter as tk
from tkinter import messagebox
import mysql.connector

# ----------- Database Connection -----------
def db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Saira@123",   # ← change this
            database="userdb"                 # ← change if different
        )
        return conn
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Connection Error:\n{e}")
        return None


#
# ----------- Check Login Function -----------
correct_username="admin"
correct_password=1234
attempts=0
def check_login():
    global attempts
    Username = entry_username.get()
    Password = entry_password.get()
    if attempts>=3:
         messagebox.showerror("blocked","your attempts are over.try again after 24hrs")
         btn.config(state="disabled")
         return
    if Username == correct_username or Password == correct_password:
        messagebox.showinfo("succecs", "login successful")
        attempts=0
    else:
        attempts+=1
        left =3-attempts
        
        if attempts>=3:
            messagebox.showerror("blocked","your attempts are over.try again after 24hrs")
            btn.config(state="disabled")    
        
        else:
            messagebox.showerror("failed",f"incorrect password\nAttempts left:{left}")

    conn = db_connection()
    if conn is None:
        return

    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (Username, Password))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        messagebox.showinfo("Login Successful", "Welcome! Login successful.")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")


# ----------- Tkinter GUI -----------
root = tk.Tk()
root.title("Login System")
root.geometry("300x250")
root.configure(bg="#e8e8e8")

# Username Label + Entry
tk.Label(root, text="Username:", font=("Arial", 12), bg="#e8e8e8").pack(pady=5)
entry_username = tk.Entry(root, font=("Arial", 12))
entry_username.pack(pady=5)

# Password Label + Entry
tk.Label(root, text="Password:", font=("Arial", 12), bg="#e8e8e8").pack(pady=5)
entry_password = tk.Entry(root, font=("Arial", 12), show="*")
entry_password.pack(pady=5)

# Login Button
btn=tk.Button(root, text="Login", font=("Arial", 12), width=10,
          command=check_login).pack(pady=15)

root.mainloop()


