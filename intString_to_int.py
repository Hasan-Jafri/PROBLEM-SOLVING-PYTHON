# Converting alphanumeric string to integer.

numeric = str(input("Enter the Alphanumeric string"))

integer = 0

for i in numeric:
    integer = integer*10 + ord(i) -ord('0') #Using ascii values.

print(integer)