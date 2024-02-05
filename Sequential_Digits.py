'''
1291. Sequential Digits

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9
'''

def sequentialDigits(low: int, high: int):
    s = '123456789'
    result = []
    for i in range(len(str(low)),len(str(high))+1):
        x = 0
        while(True):
            if x + i > len(s):
                break
            if(int(s[x:x+i]) <= high and int(s[x:x+i]) >= low ):
                result.append(int(s[x:x+i]))
            x += 1
    return result


low = int(input("Lower Range: "))
high = int(input("Higher Range: "))

print(sequentialDigits(low = low,high = high))