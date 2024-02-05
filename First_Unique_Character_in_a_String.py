'''
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
'''

def firstUniqChar(s):
    count = {}
    for i in s:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    value = ''
    for key in count.keys():
        if count[key] == 1:
            value = key
            break
    for i in range(len(s)):
        if s[i] == value:
            return i
    return -1

# Input
s = str(input())
print("First Unique Entry at index: ",firstUniqChar(s = s))