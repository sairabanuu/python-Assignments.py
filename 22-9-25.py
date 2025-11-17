list1=["red","grren","red","purple","grren","black"]
pairs=0
colors=[]
for color in list1:
    if color not in colors:
        count=0
        for c in list1:
            if c==color:
                count+=1
        pairs+=count//2
        colors.append(color)
print(pairs)

# missing values 
num=34571
num1=[3,4,5,7,1]
num1_max=max(num1)
num1_min=min(num1)
for i in range(num1_min,num1_max):
    if i not in num1:
      print(i)
        
a=[[1,2,3],[4,5,6]]
b=[[7,8,9],[1,2,3]]
rows=len(a)
cols=len(a[0])
c=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(a[i][j]+b[i][j])
    c.append(row)
for r in c:
    
  print(r)    