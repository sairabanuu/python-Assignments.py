# try:
#     num1=int(input('enter a num:'))
#     num2=int(input('enter a num:'))
#     result=num1/num2
#     print(result)
# except Exception as e:
#      print(e)
# else:
#     print()
# finally:
#     print('run the code')
    
# fibonaci by using generator
# def fibonaci(n):
#     a,b=0,1
#     for i in range(n):
#         yield a
#         a,b=b,a+b
# for num in fibonaci(10):
#     print(num)

# range by using generator
# def my_range(start,stop,step):
#     while start<stop:
#         yield start
#         start+=step
# for num in my_range(1,20,2):
#     print(num)

# class CountDown:
#     def __init__(self,start,limit,step):
#         self.num=start
#         self.limit=limit
#         self.step=step
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num>=self.limit:
#             raise StopIteration
#         current=self.num
#         self.num+=self.step
#         return current
# for i in CountDown(1,20,3):
#     print(i)

# def count_up_to(n):
#     num=1
#     while num<=n:
#         yield num
#         num+=1
# for i in range(10):
#     print(i)
        
    