# n=5
# for i in range(1,n+1):
#     for j in range(97,97+i):
#         print(chr(j), end=" " )
#     print()

# n=6
# for i in range(n):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# n=6
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# n=4
# for i in range(n):
#     for j in range(1,n+i):
#         print("*",end=" ")
#     print()

# m=3
# n=5
# for i in range(m):
#     for j in range(n):
#         print("*",end=" ")
#     print()

# n=5
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

# n=4
# for i in range(n+1):
#     for j in range(n-i):
# ``        print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()

# diamond pattrn
n=3
for i in range(1,n+1):
    print(" "*(n-i)+'*'*(2*i-1))
for i in range(n,0,-1):
      print(" "*(n-i)+'*'*(2*i-1))
print()

# buttrtfly pattern
# n=5
# for i in range(1,n+1):
#     print("*"* i, end="")
#     print(" " * (2*(n-i)), end="")
#     print("*"* i)
# for i in range(n,0,-1):
#     print("*" * i, end="")
#     print(" " * (2* (n-i)), end="")
#     print("*"* i)

# n=4
# for i in range(1,n+1):
#     # print("*" * i)
    
#     print(" " * (n-i), end="")
#     print("*"* i)
# for i in range(n-1,0,-1):
#     # print("*" * i, end="")
#     print(" " *(n-i), end="")
#     print("*" * i)

# sanddglass pattern
# n=3
# for i in range(n,0,-1):
#     print(" " * (n-i)+"*"*i)
# for i in range(2,n+1):
#     print(" " * (n-i)+"*"*i)    


# n=4
# for i in range(n):
#     for j in range(1
# ,i+1):
#         print(j,end='')
#     print()

# n=5
# for i in range(n):
#      for j in range(n-i):
#          print(" ",end=" ")
#      for j in range(i):
#          print(" * "," ",end=" ")
#      print()
# n=5
# for i in range(n-1,-1,-1):
#      for j in range(n-i):
#          print(" ",end=" ")
#      for j in range(i):
#          print(" * "," ",end=" ")
#      print()

for j in range(i):
    if(j==0 or j==i-1 or i==n-1):
        print("*"," ",end=" ")
    else:
        print(" ")
        