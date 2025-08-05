# jump statemens-pass,continue,break
# break
# for i in range(1,20):
#     print(i)
#     if i == 5:
#         break
#     print(i)
# another process

# for i in range(1,20):
#     if i<5:
#         print(i)
#         print(i)
#     elif i == 5:
#         print(i)  

# for i in range(1,31):
#     print(i*2567)
#     break  

# for i in range(1,31):
#     if i<i*(-1) or i%5==0:
#         break
#     print(i**2)

# continue-if continue statement use

# for i in range(1,34):
#     print(i)
#     print(i)
#     if i==6:
#         continue
#     print(i)

# i=5
# while i<25:
#      print(i)
#      i-=1
#      if i%5==0:
#          break
   
 
 for class_no in range(1,11):
     if class_no == 4:
         break
     for roll_no in range(1,31):
         if roll_no == 5:
             break
         print('class',class_no,'roll',roll_no)
         
     