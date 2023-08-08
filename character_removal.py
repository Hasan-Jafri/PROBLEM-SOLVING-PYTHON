# Program to remove a character based user's input from a string.

st = str(input("Enter String: "))
print("String: ", st)

letter = str(input("Enter Character to be removed: "))
# string = list(string)
# print(string)
# i = 0
# while(i < len(string)):
#     if(string[i] == letter):
#         string.remove(string[i])
#     i+=1

# print(str(string))

for i in st:
    if(i==letter):
       st= st.replace(i,'', 4)
        
print(st)
