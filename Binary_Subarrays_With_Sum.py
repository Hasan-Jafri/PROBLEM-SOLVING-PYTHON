'''
930. Binary Subarrays With Sum

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.


Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15
 

Constraints:

1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length
'''


def numSubarraysWithSum(nums, goal):
    prefix_count = {}
    current_sum = 0
    total_count = 0
    for i in nums:
        current_sum += i
        if current_sum == goal:
            total_count += 1
        if current_sum - goal in prefix_count:
            total_count += prefix_count[current_sum - goal]
        prefix_count[current_sum] = prefix_count.get(current_sum,0) + 1


    return total_count

# Sample Input
nums = [0,0,0,0,0]
goal = 0
print(numSubarraysWithSum(nums=nums,goal=goal))