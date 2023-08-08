# Program to find the level of your generation.

level = int(input())
gender = int(input())

dic = {-3:"Grand Grand Father",-2:"Grand Father",-1:"Father"
    ,0:"You",1:"Your Offspring",2:"Your Grand Offspring",3:"Grand Grand Offspring"}


if(gender == 1):
    
    print(level,":",dic[level],", Gender: Male")
elif(gender == 0):
    print(level,":",dic[level],", Gender: Female")

    