# Example 1: Convert Unicode code points to characters
print(chr(65))  # Output: 'A'
print(chr(8364))  # Output: '€'
print(chr(128516))  # Output: '😄'

# Example 2: Generate a string from a list of Unicode code points
code_points = [72, 101, 108, 108, 111]
string = ''.join(chr(cp) for cp in code_points)
print(string)  # Output: 'Hello'