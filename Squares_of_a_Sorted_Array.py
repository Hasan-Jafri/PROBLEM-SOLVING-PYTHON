'''
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
'''

def sortedSquares(nums):
# Average Method. O(nlog(n))
    nums = [i*i for i in nums]
    nums.sort()
    return nums
# O(n) Method.
    # n = len(nums)
    # ans = [0] * n
    # start = 0
    # end = n-1
    # for i in range(n-1,-1,-1):
    #     if abs(nums[start]) >= abs(nums[end]):
    #         ans[i] = nums[start] * nums[start]
    #         start += 1
    #     else:
    #         ans[i] = nums[end] * nums[end]
    #         end -= 1
    # return ans

# Sample Input
nums = [-4,-1,0,3,10]
print(sortedSquares(nums = nums))
