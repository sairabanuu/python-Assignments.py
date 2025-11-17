# checck the duplicates
def check_duplicates(lst):
    result=[]
    for num in lst:
        digits=str(num)
        if len(set(digits))<len(digits):
            result.append(True)
        else:
            result.append(False)
    return result
numbers=[202,89,112,88]
print(check_duplicates(numbers))

# or

numbers=[202,89,112,88]
result=[]
for num in numbers:
    digits=str(num)
    if len(set(digits))<len(digits):
         result.append(True)
    else:
      result.append(False)
print(result)

# sum of matrix
def sum_matrix(matrix):
    total=0
    for row in matrix:
        total+=sum(row)
    return total
mat=[[1,2,3],[4,5,6],[7,8,9]]
print(sum_matrix(mat))

# or

matrix=[[1,2,3],[4,5,6],[7,8,9]]
total=0
for row in matrix:
    for num in row:
        total+=num
        
print(total)
