'''
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

def minWindow(s, t):
    result = ""
    l = 0
    r = 0
    counter = {}
    # Counting the values in t.
    for i in t:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    # Storing the no.of unique variable in the string t in overall.
    overall = len(counter)
    while r < len(s):
        if s[r] in counter:
            counter[s[r]] -= 1
            if counter[s[r]] == 0:
                overall -= 1
        # Loop to figure out the minimum string.
        while overall == 0:
            if not result:
                result = s[l:r+1]
            elif (r - l + 1) < len(result):
                result = s[l:r+1]
            # Decreasing window size.
            if s[l] in counter:
                counter[s[l]] += 1
                if counter[s[l]] > 0:
                    overall += 1
            l += 1
        r += 1
    return result
        
s = str(input("Input s: "))
t = str(input("Input t: "))
print("Minimum Window Substring: ",minWindow(s , t))