# def circle(r,pie):
#     print('area of circle')
#     print(pie*r*r)
# circle(10,3.15)
# circle(20,4.14)
# circle(30,5.14)
# in this pgm we wrire parameters and arguments in def we write r that is parameter and the calling a function we write a values that is argumets.we run the code then the value of r
# def calci(a,b):
#     print(a+b)
#     print(a-b) 
#     print(a*b)
#     print(a%b)
#     # print(a/b)
#     if b!=0:
#           print(a/b)
#     else:
#         print('not possible')
# calci(2,3)
# calci(3,4)
# calci(4,5)
# calci(6,7)
# calci(8,9)

# def table(n):
#    for i in range(1,11):
#      print(n,'*',i,'=',n*i)
# table(4)   

# def naturalnum():
#     sum=0
#     for i in range(1,11):        
#       sum+=i
#       print(i)
#     print(sum) 
# naturalnum()
# or
# def sum_of_num(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     print(sum)
# sum_of_num(8)    

# def product(n):
#     sum=0
#     for i in range(1,n*1):
#         sum+=i
#     print(sum)
# product(5) 

# def sum_number(a,*args,c):
#           temp=a,c
#           for i in args:
#               temp=temp+i
#           print(temp)
# sum_number(2,3,4,5) 
          #the arbitary argument pgm
# def sum_number(a,b,c):
#     print(a+b+c)
# def sum_number(a,b,c,d):
#     print(a+b+c+d)
# sum_number(1,2,3,4)
# sum_number(1,2,3)
# sum_number(1,2,3,4)

# def sum(a,b):
#    print(a+b)
# sum(2,3)

# def square(a):
#     print(a**2)
# square(2)

# def even(a):
#     if a%2==0:
#         print('even')
#     else:
#         print('odd') 
# even(4)   

# def factors(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)
# factors(6)    
    
# def factorial_number(n=9):
#     fact=1
#     for i in range(1,n+1):
#       fact*=i
#     print(fact)
# factorial_number(5)

# def maximum(a,b,c):
    
#     if a>b and a>c:
#         print(a)
#     elif b>a and b>c:
#         print(b)
#     else:
#         print(c)
# maximum(3,4,5)

# def vowels(str1):
#     count=0
#     for ch in str1:
#         if ch in 'aeiou':
#             count+=1
#     print(count)
# vowels('saira')

# def list():
#     sum=0
#     l1=[1,2,3,4]
#     for i in l1:
#         sum+=i
#     print(sum)
# list()
     
# def reverse():
#     s='saira'
#     print(s[::-1])
# reverse()

# def palindrome():
#     a='madam'
#     if a==a[::-1]:
#         print('palindrome')
#     else:
#         print('no')
# palindrome()

# def list_even():
#     l1=[2,3,4,6,7,8]
#     for i in l1:
#         if i%2==0:
#             print(i)
# list_even()

# def circle(r,pie):
#    print('area of circle')
#    print(pie*r*r)
# circle(15,3.14)

# def len():
#     count=0
#     a='sairabanu'
#     for i in a:
#         count+=1
#     print(count)
# len() 

# def Avg(num1,num2,num3):
#     Average=(num1+num2+num3/3)
#     print(Average)
# Avg(3,4,5)

# # keyword arbitary arguments
# def connect_to_db(*args):
#     print(args)
# connect_to_db('licalhost:3000','2345','3000','2243')

# def connect_to_db2(**kargs):
#     print(kargs)
# connect_to_db2(db_loc='localhost:3000',db_pool='2345',db_port='3330',db_password='2243')

# return
# def add(n1,n2):
#     return n1+n2
# result=add(2,3)
# print(result)
         
# def even_odd(n1,n2):
#     if n1%2==0 and n2!=0:
#         return 'even'
#     else:
#         return 'odd'
# res=even_odd(5,3)
# print(res)

# def cal(a,b):
#     return a+b,a*b,a-b
# r1=cal(4,5)
# print(r1)

# def list():
#     l2=[2,3,4]
#     # for i in l2:
#     return l2
# l=list()
# print(l)    
        
