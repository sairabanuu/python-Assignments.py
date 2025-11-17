def print_reverse(lst, index):
    if index < 0:
        return
    print(lst[index])
    print_reverse(lst, index - 1)

lst = [10, 20, 30, 40, 50]
print_reverse(lst, len(lst)-1)


def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)


# Driver code
a = int(input("Enter base: "))
b = int(input("Enter exponent: "))

print("Result:", power(a, b))
