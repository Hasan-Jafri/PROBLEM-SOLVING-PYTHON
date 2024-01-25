'''
1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
'''

# I utilized a Dynamic Programming approach towards this problem
# I created a 2d dp array of n+1 x m+1 length and filled it with 0s initially
# After that I iterated through the strings and when I found out the common characters, I incremented the above value by 1.
# If the character does not match it takes the max of its above and previous values.
# At the end I return the answer from the array.
# The solution has a complexity of O(n^2)

def longestCommonSubsequence(text1: str, text2: str) -> int:
    if len(text2) > len(text1):
        text1 , text2 = text2, text1
    dp = []
    for i in range(len(text1)+1):
        temp = []
        for j in range(len(text2)+1):
            temp.append(0)
        dp.append(temp)
    for i in range(len(text1)):
        for j in range(len(text2)):
            if text1[i] == text2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[len(text1)-1][len(text2)-1]


# Input
text1 = str(input("String 1: "))
text2 = str(input("String 2: "))
print("Longest Subsequence Length: ",longestCommonSubsequence(text1=text1,text2=text2))