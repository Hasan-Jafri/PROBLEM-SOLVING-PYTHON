# Program to find if two  string are anagram or not.



string_1 = str(input("Enter String 1: "))

string_2 = str(input("Enter String 2: "))

# count = 0
# if(len(string_1) == len(string_2)):
    
#     for i in string_1:
#         for j in string_2:
#             if(i == j):
#                 count += 1
# else:
#     print("Not Anagram")
    
# if(count == len(string_1)):
#     print("Anagram")
# else:
#     print("Not Anagram")
flag = True  
dct = {}  
for i in string_1:
    if(i not in dct):
        dct[i] = 1
    else:
        dct[i] += 1
        
for j in string_2:
    if(j not in dct):
        flag = False
        break
    else:
        dct[j] +=1

if(flag == True):
    for i in dct:
        if(dct[i] == 2):
            continue
        else:
            flag = False
if(flag == True):
    print("Anagram")
else:
    print("Not Anagram")
    
    