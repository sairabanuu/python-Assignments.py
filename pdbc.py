import mysql.connector
conn = mysql.connector.connect(
    host="localhost",      
    user="root",           
    password="your_password",  # your MySQL root password
    database="school"      # database name
)
cursor = conn.cursor() 
cursor.execute()
# Create Database s Table
cursor.execute("CREATE DATABASE IF NOT EXISTS my_database")

create_table = """
CREATE TABLE IF NOT EXISTS students ( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100),
email VARCHAR(100) UNIQUE,
course VARCHAR(100), joined_date DATE
) """
cursor.execute(create_table)
# Single Record
query = """INSERT INTO students(name,email,course,joined_date) VALUES (%s,%s,%s,%s)"""
cursor.execute(query, ('Nandu','nandu@gmail.com','PFS','2025-06-08')) 
# Multiple Records
data = [
('John','john@gmail.com','JFS','2025-04-05'),
('Suman','suman@gmail.com','JFS','2025-05-05'),
('Rakesh','rakesh@gmail.com','DS','2025-02-06')
]
cursor.executemany(query, data)
conn.commit()
# Read / Fetch Records
# Fetch All
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall(): 
 print(row)
# Fetch Limited
cursor.execute("SELECT * FROM students LIMIT 2") 
print(cursor.fetchall())
# Fetch Ordered
cursor.execute("SELECT * FROM students ORDER BY name ASC") 
print(cursor.fetchall())
# Fetch Specific Columns
cursor.execute("SELECT name, course FROM students")
for row in cursor.fetchall(): print(row)
# Fetch with Condition
cursor.execute("SELECT * FROM students WHERE course = %s", ('DS',))
for row in cursor.fetchall(): 
 print(row)
# Update a Student’s Course by Email
update_query = "UPDATE students SET course = %s WHERE email = %s" cursor.execute(update_query, ("Data Science", "nandu@gmail.com")) 
conn.commit()
# Update Multiple Columns Together
update_query = """UPDATE students
SET name = %s, course = %s WHERE id = %s"""
cursor.execute(update_query, ("Nandu Kumar", "AI/ML", 1)) 
conn.commit()

# Update Based on Condition
cursor.execute("UPDATE students SET course = %s WHERE course = %s", ("GenAI", "DS"))
conn.commit()
# Delete by ID
cursor.execute("DELETE FROM students WHERE id = %s", (3,)) 
conn.commit()
# Delete by Email
cursor.execute("DELETE FROM students WHERE email = %s", ("john@gmail.com",)) 
conn.commit()
# Delete All Records (Dangerous!)
cursor.execute("TRUNCATE TABLE students")
conn.commit()

