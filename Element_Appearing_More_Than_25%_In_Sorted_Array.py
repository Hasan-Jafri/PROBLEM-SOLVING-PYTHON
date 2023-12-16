'''
1287. Element Appearing More Than 25% In Sorted Array

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 105
'''

def findSpecialInteger(arr):
        value = int(0.25*len(arr))
        if(len(arr) <= 2):
            return arr[0]
        else:
            count = 1
            result = 0
            for i in range(1,len(arr)):
                if(arr[i] == arr[i-1]):
                    count += 1
                else:
                    count = 1
                if(count > value):
                    result = arr[i-1]
            return result
size = int(input("Size of Input Array: "))
nums = []
for i in range(size):
    input_ = int(input(":"))
    nums.append(input_)

print("The Element appearing more than 25%: ",findSpecialInteger(arr=nums))