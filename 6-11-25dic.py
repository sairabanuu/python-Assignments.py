first = input("Enter first string: ")
second = input("Enter second string: ")

found = False
start_index = -1

for i in range(len(first) - len(second) + 1):
    match = True
    for j in range(len(second)):
        if first[i + j] != second[j]:
            match = False
            break
    if match:
        found = True
        start_index = i
        break

if found:
    print("Substring found at index:", start_index)
else:
    print("Not a substring")


s = input("Enter a string: ")

largest = ""
current = ""

for ch in s:
    if ch != " ":       # character is part of a word
        current += ch
    else:               # word ended
        if len(current) > len(largest):
            largest = current
        current = ""

# check last word also
if len(current) > len(largest):
    largest = current

print("Largest word:", largest)
print("Length:", len(largest))
