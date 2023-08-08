# Program to find the second largest element from the given array.

array = [2,8,4,6,4,5,77,44,99]

largest = 0
second_largest = 0
flag = False
for i in array:
    if(i > largest):
        flag = True
    elif(i > second_largest):
        second_largest = i
    if(flag == True):
        if(second_largest < i):
            second_largest = largest
        largest = i
        flag = False

        
        
print(second_largest)