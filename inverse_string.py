# Program to find the inverse of a string.

string = str(input("Enter a sentence: "))
answer = ""
reverse = ""
array =[]
word = ""

#This loop print the string in reverse order.
# for i in range(len(string)):
#     word += string[i]
    
#     if(string[i] == " "):
#         reverse = word + reverse
#         word=""
# reverse = word + " "+ reverse 
# word = ""
# print(reverse) 


#This loop works
for i in range(len(string)-1,-1,-1):
    word += string[i]
    
    if(string[i] == " "):
        answer += word 
        word=""
answer += word
    
print(answer)