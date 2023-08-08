# Finding if the given string is a palindrome or not.

string = str(input("Enter String: "))


if(string[:] == string[::-1]):
    print("Palindrome")
else:
    print("Not Palindrome")