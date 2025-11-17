s = "(a+b-c*[e/f])"

res = ""
for ch in s:
    if ch not in "(){}[]":
        res += ch

print(res)


s = "python"
rev = ""
for i in range(len(s)-1, -1, -1):
    rev += s[i]
print(rev)


s = input("Enter a string: ")

vowels = "aeiouAEIOU"
v = c = sp = 0

for ch in s:
    if ch in vowels:
        v += 1
    elif ch == " ":
        sp += 1
    elif ch.isalpha():   # consonant
        c += 1

print("Vowels:", v)
print("Consonants:", c)
print("Spaces:", sp)
