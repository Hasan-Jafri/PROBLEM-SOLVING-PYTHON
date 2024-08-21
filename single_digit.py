# Converting a number into a single digit using the 
# method of adjacent  subtaction repeatedly until one element
# is left and that element is the final answer

num = 16784 # Number to be manipulated

lst = [] # Initializing list to store differences
num = list(str(num)) # Converting num into a string list for iteration.
print(num)

while(len(num) != 1):
    temp = 0 # Initializing variable to claculate difference and stor in lst.
    for i in range(1,len((num))):
        temp = abs(int(num[i]) - int(num[i-1])) # calculating difference of current element with previous.
        lst.append(temp) # Appending temp value in lst.
        temp = 0 # Making temp 0 for next iteration.
    num = lst # Giving num the values stored in lst for itertion.
    print(num)
    lst = [] # Emptying the lst to sotre the next iteration differences.
print(num[0]) #After whole process is finished we are left with a single element un the num which is our result.