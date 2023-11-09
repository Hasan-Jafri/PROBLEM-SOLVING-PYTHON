'''
1679. Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
'''

def maxOperations(nums, k):
    nums.sort()
    left = 0
    pair = 0
    right = len(nums) - 1

    while(left < right):
        if(nums[left] + nums[right] == k):
            # print(nums[left],nums[right])
            nums.pop(right)
            nums.pop(left)
            right -= 2
            pair += 1
        elif nums[left] + nums[right] < k:
            left += 1
        else:
            right -= 1

    return pair


size = int(input("Size of Input Array: "))
nums = []
for i in range(size):
    # Make sure to input 1s and 0s only.
    input_ = int(input(":"))
    nums.append(input_)
k = int(input("Enter K: "))


print(maxOperations(nums=nums,k=k))