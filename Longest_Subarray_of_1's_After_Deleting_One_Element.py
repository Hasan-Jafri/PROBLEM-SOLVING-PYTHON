'''
1493. Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.x
Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
'''

def longestSubarray(nums):
    largest = 0
    if 0 not in nums:
        return len(nums)-1
    else:
        string = ''.join(map(str,nums))
        lst = string.strip().split('0')
        result = []
        for i in range(1,len(lst)):
            count = len(lst[i] + lst[i-1])
            largest = max(largest,count)

        return largest
    
n = int(input("Array Length: "))
nums = []
for i in range(n):
     input_ = int(input(": "))
     nums.append(input_)
print(longestSubarray(nums=nums))