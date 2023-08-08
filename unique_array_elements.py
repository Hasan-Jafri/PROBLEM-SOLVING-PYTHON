'''The Task here is to identify the same numbers in both arrays 
and put them in the 'same' named array.If an element is unique in both the arrays
then append that element in different array'''

arr1 = [1,2,3,4,5]

arr2 = [2,3,1,0,5]

same = []
different = []

# Mehtod Using Dictionary.
# dct = {}

# for i in arr1:
#     if(i not in dct):
#         dct[i] = 1
#     else:
#         dct[i] += 1
        
# for j in arr2:
#     if(j in dct):
#         dct[j] += 1
#     else:
#         dct[j] = 1
        
# for i in dct:
#     if(dct[i] == 1):
#         different.append(i)
#     else:
#         same.append(i)
# Method using nested loop.
for i in arr1:
    present = False
    for j in arr2:
        if(i == j):
            present = True
    if(present == True):
        same.append(i)
    else:
        different.append(i)
            
for i in arr2:
    if(i not in same):
        different.append(i)
              

# print(dct)

print("Elemets same in both arrays: ",same)

print("Elements unique in both arrays: ",different)