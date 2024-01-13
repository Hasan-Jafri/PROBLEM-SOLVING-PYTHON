'''
1347. Minimum Number of Steps to Make Two Strings Anagram


You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
 

Constraints:

1 <= s.length <= 5 * 104
s.length == t.length
s and t consist of lowercase English letters only.
'''

def minSteps(s: str, t: str) -> int:
    if (len(s) != len(t)):
        return 0
    count = {}
    for i in s:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    remove = len(s)
    for char in t:
        if char in s and count[char] > 0:
            count[char] -= 1
            remove -= 1
        
    return remove


# Input
s = str(input("s : "))
t = str(input("t : "))
print(minSteps(s = s,t = t))