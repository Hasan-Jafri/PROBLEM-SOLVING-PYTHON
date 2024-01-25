# Given the length of a rod find the maximum price it can be sold into pieces.
# You are given with cut size and its price.
# Example length = 4
# Cut =   1 2 3 4
# Price = 1 5 8 9
# So it should return 10.

def Rod_Cutting_Bottom_Up(length, price_array):
    cost = 4
    s = [0]*11
    dp = [0]
    for i in range(1,length+1):
        max_val = -10000
        for j in range(i):
            k = max_val

            max_val = max(max_val, price_array[j] + dp[i - j - 1])
            if k != max_val:
                s[i] = j
        
        dp.append(max_val)
    print(s)
    print("Cuts: ",s[length-1])
    return dp[length]


price_array = [1,5,8,9,10,17,17,20,24,30]
length = 8
print(Rod_Cutting_Bottom_Up(length=length,price_array=price_array))