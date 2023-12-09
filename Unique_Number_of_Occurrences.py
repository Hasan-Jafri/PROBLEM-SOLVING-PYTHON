'''
1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
'''

def uniqueOccurrences(arr):
    occur_dict = {}
    sample = []
    for i in arr:
        if i not in occur_dict:
            occur_dict[i]  = 1
        else:
            occur_dict[i] += 1
    for value in occur_dict.values():
        if value not in sample:
            sample.append(value)
        else:
            return False
    return True

n = int(input("Array Length: "))
nums = []
for i in range(n):
     input_ = int(input(": "))
     nums.append(input_)
print(uniqueOccurrences(arr=nums))