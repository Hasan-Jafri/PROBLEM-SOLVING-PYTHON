'''
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
'''
def findMaxAverage(nums, k):
    summ = 0
    avg = []
    counter = 0
    start = 0
    for i in range(len(nums)):
        counter += 1
        summ += nums[i]
        if(counter == k):
            print(summ)
            avg.append(summ/k)
            counter = k-1
            summ -= nums[start]
            start += 1
        
    return max(avg)

size = int(input("Size of Input Array: "))
nums = []
for i in range(size):
    # Make sure to input 1s and 0s only.
    input_ = int(input(":"))
    nums.append(input_)
k = int(input("Enter Subarray Size: "))

print(findMaxAverage(nums=nums,k=k))