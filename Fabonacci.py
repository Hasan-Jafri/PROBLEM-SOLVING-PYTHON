# Program to print n elemets of the Fabonacci series.

n = int(input("Enter number of elments: "))
num1 = 0
num2 = 1
Fabonacci = []
Fabonacci.append(num1)
Fabonacci.append(num2)
if(n==1):
    print(Fabonacci[0])
elif(n==2):
    print(Fabonacci)
elif(n>2):
    
    for i in range(n):
        sum = num1 + num2
        Fabonacci.append(sum)
        num1 = num2
        num2 = sum
    print(Fabonacci)
else:
    print("Invalid Input.")