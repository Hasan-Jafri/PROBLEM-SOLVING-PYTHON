'''
2610. Convert an Array Into a 2D Array With Conditions

You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.


Example 1:

Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]
Explanation: We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.
Example 2:

Input: nums = [1,2,3,4]
Output: [[4,3,2,1]]
Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= nums.length
'''

def findMatrix(nums):
    result = []
    count = {}
    for i in nums:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    while(True):
        temp = []
        end = True
        for key, value in count.items():
            if count[key] >= 1 and key not in temp:
                end = False
                count[key] -= 1
                temp.append(key)
        if end == True:
            break
        result.append(temp)
        
    return result

# Example Input
nums = [1,3,4,1,2,3,1]
print(findMatrix(nums=nums))