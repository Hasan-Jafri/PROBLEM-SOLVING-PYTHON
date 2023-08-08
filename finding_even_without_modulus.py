# Program to find even or odd numbers without the use of modulus.

num = 15
temp = num

while(True):
    if(num == 0 or num ==1):
        break
    else:
        num = num -2
    
if(num == 0):
    print("Even")
else:
    print("Odd")