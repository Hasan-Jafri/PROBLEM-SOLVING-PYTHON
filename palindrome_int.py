# Program to find if the given number is a palindrome or not.

num1 = int(input("Enter Number:"))

check = num1


rev = 0
while(num1 > 0):
    rem = num1 % 10
    rev = rev*10 + rem
    num1 = num1//10

if(check == rev):
    print("Palindrome")
else:
    print("Not a palindrome")