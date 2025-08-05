# i=1
# while i <=10:
#     print("7 *",i,"=",7*i)
#     i+=1

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
    
# n=int(input('enter a num:'))
# for i in range(1,n+1):
#     print('*'*i)
#     i+=1

# n=int(input('enter a no:'))
# s=65
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(s),end=" ")
#     s+=1 
#     print()    
#     i+=1

# num=int(input('enter a no:'))
# if num%2==0:
#     print(num,'even')
# else:
#     print('odd')

# num1=int(input('enter a no:'))
# num2=int(input('enter a no:'))
# if num1>num2:
#     print(num1)
# else:
#     print(num2)


# num1=int(input('enter a no1:'))
# num2=int(input('enter a no2:'))
# num3=int(input('enter a no3:'))
# if num1>num2>num3:
#     print(num1)
# elif num1<num3:
#     print(num3)
# else:
#     print(num2)

# n=int(input('enter a no:'))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# n=int(input('enter a no:'))
# for i in range(1,n+1):
#     if i%2==0:
#         print(i)
    
# num=int(input('enter a no:'))
# for i in range(1,num+1):
#     for j in range(1,11):
#        print(i,'*',j,'=',i*j)

# i=1
# count=0
# while(i<=10):
#    count+=1
#    print(i)
#    i+=1
# print(count)

# num=1234
# sum=0
# while num<=10:
#     sum+=num
# print(sum)

# num=123
# sum=0
# while(num!=0):
#    rem=num%10
#    sum+=rem
#    num//=10
# print("sum:",sum)

# for i in range(0,4):
#    pass_word=(input("enter a password"))
#    if pass_word=="12345":
#      print("Login Successful")
# else:
#      print("Accont locked")

# number=(input("enter a number"))
# for i in number:
#     digit=int(i)
#     if digit!=0: 
#         print(digit)
#     else:
#         break
    
# for i in range(1,21):
#     if i%3==0:
#      continue
#     print(i)
    
# while True:
#   num1=int(input("enter a number:"))
#   if num1==0:
#      break
#   else:
#      print(num1)

# even_count=0
# odd_count=0
# for i in range(5):
#   num1=int(input("enter a number:"))
#   if num1%2==0:
#      even_count+=1
#   else:
#      odd_count+=1
# print("even numbers:",even_count)
# print("odd numbers:",odd_count)

# str1=input("enter a string:")
# for i in str1:
#    print(i)

num1=int(input("enter a number:"))
if num1%2==0 and num1%5==0:
  print(num1,"is divisible by 2 and 5:")
elif num1%2==0:
  print(num1,"is divisible by 2 not by 5 ")
else:
  print(num1,"is not divisible by both 2 and 5")
