# Program to find the largest frequency of a character in a string.

string = 'wdhfflhdfowufkadjf'

dic = {}
for i in string:
    if(i not in dic):
        dic[i] = 1
    else:
        dic[i] += 1


char = string[0]
for i in string:
    if(dic[char] < dic[i]):
        char = i
        
print(char)
        