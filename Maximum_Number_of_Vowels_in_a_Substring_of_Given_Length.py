'''
1456. Maximum Number of Vowels in a Substring of Given Length.

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
'''


def maxVowels(s, k):
    maximum = 0
    left = 0
    count = 0
    vowels = ['a','e','i','o','u']

    for i in range(k):
        if s[i] in vowels:
            count += 1
    maximum = max(count,maximum)
    i = k
    while i < len(s):
        if s[i] in vowels:
            count += 1
        if s[left] in vowels:
            count -= 1
        maximum = max(count,maximum)
        i += 1
        left += 1

    return maximum  

s = str(input())
k = int(input())
print(maxVowels(s=s,k=k))