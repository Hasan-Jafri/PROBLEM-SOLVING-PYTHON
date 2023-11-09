'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''

def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if(len(nums) == 0 or len(nums) == 1):
            return nums
        elif(0 not in nums):
            return nums
        else:
            i = 0
            while(True):
                if(nums[i] == 0):
                    nums.append(0)
                    nums.remove(0)
                i += 1
                if(i == len(nums)):
                    break
        return nums

n = int(input("Array Length: "))
nums = []
for i in range(n):
     input_ = int(input(": "))
     nums.append(input_)

print(moveZeroes(nums))
