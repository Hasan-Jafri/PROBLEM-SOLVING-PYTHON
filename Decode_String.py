'''
394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
'''
# Stack Approach.

def decodeString(s: str) -> str:
        stack = []
        current_num = 0
        current_str = ''
        for i in s:
            if i.isdigit():
                current_num = current_num*10 + int(i)
            elif i == '[':
                stack.append(current_num)
                stack.append(current_str)
                # Resetting the values.
                current_num = 0
                current_str = ''
            elif i == ']':
                previous_str = stack.pop()
                previous_num = stack.pop()
                # Values stored in stack will be used.
                current_str = previous_str + current_str*previous_num
            else:
                current_str += i
        return current_str

# Input
s = str(input(": "))
print(decodeString(s = s))