def print_natural(n):
    if n == 0:
        return
    print_natural(n - 1)
    print(n)


n = int(input("Enter n: "))
print_natural(n)

def print_reverse(n):
    if n == 0:
        return
    print(n)
    print_reverse(n - 1)


n = int(input("Enter n: "))
print_reverse(n)

def print_even(n):
    if n == 0:
        return
    print_even(n - 1)
    print(2 * n)


n = int(input("Enter n: "))
print_even(n)

