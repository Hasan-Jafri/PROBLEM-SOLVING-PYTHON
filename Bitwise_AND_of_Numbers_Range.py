'''
201. Bitwise AND of Numbers Range

Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

 

Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0

Constraints:

0 <= left <= right <= 231 - 1
'''
# BitShift Approach.

def rangeBitwiseAnd(left, right):
    count = 0
    while(right != left):
        count += 1
        right = right>>1
        left = left>>1

    return left<<count

# Input
left = int(input())
right = int(input())
print(rangeBitwiseAnd(left = left,right = right))