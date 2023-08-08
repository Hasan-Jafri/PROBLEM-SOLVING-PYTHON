# Program to find the largest two elements that sum together to form the required sum.
array = [2,3,1,0,5,4] # Given Array.

req = 6 # Requuired Sum.
element1 = 0
element2 = 0
for i in range(len(array)):
    j = i
    while(j <len(array)):
        
        if(array[i]+array[j] == req and j != i):
            if(array[i] > element1 and array[j] > element2 and i!=j):
                element1 = array[i]
                element2 = array[j]
        j+=1
                
print(element1,element2)

