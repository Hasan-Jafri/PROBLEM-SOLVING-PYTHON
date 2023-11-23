'''
1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
'''

def longestOnes(nums, k):
    maximum = 0
    i = 0
    j = 0
    zero_counter = 0
    while j < len(nums):
        if nums[j] == 0:
            zero_counter += 1
        if zero_counter > k:
            if nums[i] == 0:
                zero_counter -= 1
            i += 1
        if zero_counter <= k:
            maximum = max(maximum,j-i+1)
        j += 1
    return maximum

n = int(input("Array Length: "))
nums = []
for i in range(n):
     input_ = int(input(": "))
     nums.append(input_)
k = int(input("Enter k: "))

print(longestOnes(nums,k))