'''
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?

'''

def majorityElement(nums):
# Solution using O(n) time and O(n) space.
    # count = {}
    # for i in nums:
    #     if i not in count:
    #         count[i] = 1
    #     else:
    #         count[i] += 1
    # for i in count.keys():
    #     if count[i] > int(len(nums)/2):
    #         return i
# Solution using O(n) time, but O(1) sapce.
    result = nums[0]
    majority = 0
    for i in nums:
        if majority == 0:
            result = i
        if i == result:
            majority += 1
        else:
            majority -= 1
    return result

# Input.
nums = [2,2,1,1,1,2,2]
print(majorityElement(nums = nums))