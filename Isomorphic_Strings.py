'''
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
'''

def isIsomorphic(s, t):
    mapping_s = {}
    mapping_t = {}
    for i in range(len(s)):
        if s[i] not in mapping_s and t[i] not in mapping_t:
            mapping_s[s[i]] = t[i]
            mapping_t[t[i]] = s[i]
        elif s[i] in mapping_s and mapping_s[s[i]] != t[i]:
            return False
        elif t[i] in mapping_t and mapping_t[t[i]] != s[i]:
            return False
    return True 

# Sample Input
s = "bbbaaaba"
t = "aaabbbba"
print(isIsomorphic(s=s,t=t)) 