'''
You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, 
where 0 means empty and 1 means not empty, and an integer n, 
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
'''


def canPlaceFlowers(flowerbed, n):
        result = []
        count = 0
        if(len(flowerbed) > 1):
            if(flowerbed[0] == 0 and flowerbed[1] == 0):
                flowerbed[0] = 1
                count += 1
            for i in range(1, len(flowerbed)-1):
                if(flowerbed[i] == 0):
                    if(flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
                        count += 1
                        flowerbed[i] = 1
            if(flowerbed[len(flowerbed) -1] == 0 and flowerbed[len(flowerbed)-2] == 0):
                flowerbed[len(flowerbed)-1] = 1
                count += 1
        else:
            if(flowerbed[0] == 0):
                count += 1

        if(count >= n):
            return True
        return False

size = int(input("Size of flowerbed: "))
flowerbed = []
for i in range(size):
    # Make sure to input 1s and 0s only.
    input_ = int(input(":"))
    flowerbed.append(input_)
n = int(input("Enter flowers to pot: "))
print(flowerbed)
print(canPlaceFlowers(flowerbed=flowerbed, n=n))