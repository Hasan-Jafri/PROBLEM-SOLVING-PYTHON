'''
525. Contiguous Array

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.


Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''

def findMaxLength(nums):
    summs = {}
    summ = 0
    maxlen = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            summ -= 1
        else:
            summ += 1
        
        if summ == 0:
            maxlen = max(maxlen,i + 1)
        elif summ in summs:
            maxlen = max(maxlen,i - summs[summ])
        else:
            summs[summ] = i
    return maxlen

# Sample Input
nums = [0,0,1,0,0,0,1,1]
print(findMaxLength(nums=nums))