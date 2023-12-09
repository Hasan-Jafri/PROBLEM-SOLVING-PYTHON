'''
2215. Find the Difference of Two Arrays

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
Example 2:

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].

Constraints:

1 <= nums1.length, nums2.length <= 1000
-1000 <= nums1[i], nums2[i] <= 1000
'''

def findDifference(nums1, nums2):
    answers = []
    temp = []
    for i in nums1:
        if i not in nums2 and i not in temp:
            temp.append(i)
    answers.append(temp)
    temp = []
    for j in nums2:
        if j not in nums1 and j not in temp:
            temp.append(j)

    answers.append(temp)

    return answers


n = int(input("Array 1 Length: "))
nums1 = []
for i in range(n):
     input_ = int(input(": "))
     nums1.append(input_)
n = int(input("Array 2 Length: "))
nums2 = []
for i in range(n):
     input_ = int(input(": "))
     nums2.append(input_)
print(findDifference(nums1=nums1,nums2=nums2))