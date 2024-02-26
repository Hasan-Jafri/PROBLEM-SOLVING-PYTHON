'''
231. Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
 

Constraints:

-231 <= n <= 231 - 1
'''

def isPowerOfTwo(n):
# One Solution O(logn)
#    ispower = False
#    power = 1
#    while(power <= n):
#        if(power == n):
#            ispower = True
#            break
#        else:
#            power *= 2
#    return ispower
# Without Loops and Recursions O(1)
# We can use bitwise AND and if it zero then we return true
    return n > 0 and n & (n-1) == 0

# Input
n = int(input())
print("Power of 2: ",isPowerOfTwo(n = n))