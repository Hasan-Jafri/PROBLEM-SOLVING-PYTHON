'''
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 
Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''

def isAnagram(s,t):
    
    check_s = {}
    check_t = {}

    n = 0
    while(n < max(len(s),len(t))):
        if(n < len(s)):
            if s[n] in check_s:
                check_s[s[n]] += 1
            else:
                check_s[s[n]] = 1

        if(n < len(t)):
            if t[n] in check_t:
                check_t[t[n]] += 1
            else:
                check_t[t[n]] = 1   
        n += 1
    if(check_s == check_t):
        return True
    return False    

# Sample Input.
s = "anagram"
t = "nagaram"

print(isAnagram(s=s,t=t))