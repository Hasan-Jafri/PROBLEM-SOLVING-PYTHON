'''
2444. Count Subarrays With Fixed Bounds

You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
Example 2:

Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
 

Constraints:

2 <= nums.length <= 105
1 <= nums[i], minK, maxK <= 106
'''


def countSubarrays(nums, mink, maxK):
    count = 0
    left = 0
    right = 0
    mini = -1
    maxi = -1
    while right < len(nums):
        if nums[right] == mink:
            mini = right
        if nums[right] == maxK:
            maxi = right
        if nums[right] < mink or nums[right] > maxK:
            left = right + 1
        count += max(min(mini,maxi) - left + 1, 0)
        right += 1
    return count

# Sample Input
nums = [1,3,5,2,7,5]
minK = 1
maxK = 5
print(countSubarrays(nums=nums,maxK=maxK,mink=minK))