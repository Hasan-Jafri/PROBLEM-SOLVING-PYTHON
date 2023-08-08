# Program to find non repeating characters in a string.

string = 'mynameisshabbi'

# Solution using list
# lst = []

# for i in string:
#     if(i not in lst):
#         lst.append(i)
#     else:
#         lst.remove(i)
        
# print(lst)

# Solution using dictionary
dct = {}

for i in string:
    if(i not in dct):
        dct[i] = 1
    else:
        dct[i] += 1

for i in dct:
    if(dct[i] == 1):
        print(i)