def my_range(start,stop,step):
    while start<stop:
        yield start
        start+=step
for num in my_range(1,20,2):
    print(num)
    
def fibonaci(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b
for num in fibonaci(10):
    print(num)
    
    
    
num=[1,2,3]
it=iter(num)
print(next(it))
print(next(it))
print(next(it))

# custom iterator
class CountDown:
     def __init__(self,start):
        self.num=Start
     def __iter__(self):
         return self
     def __next__(self):
         if self.num<0:
              raise stopiteration   
         current=self.num
         self.num-=1
         return current
for i in CountDown(5):
         print(i)
         
# generator
def count_up_to(n):
    num=1
    while num<=n:
        yield num
        num+=1
for i in count_up_to(5):
    print(i)
    
def gen():
    yield 1
    yield 2
    yield 3
var=gen()
print(next(var))
print(next(var))
print(next(var))

