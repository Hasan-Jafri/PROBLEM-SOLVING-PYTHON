'''
85. Maximal Rectangle


Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.

'''

def maximalRectangle(matrix):
    heights = [0] * (len(matrix[0]) + 1)
    rows = len(matrix)
    cols = len(matrix[0])
    area = 0

    for row in matrix:
        for i in range(cols):
            if row[i] == '0':
                heights[i] = 0
            else:
                heights[i] += 1
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = max(area, height * (i - index))
                start = index
            stack.append([start,h])

        for i,h in stack:
            area = max(area,h * (len(heights)-i))
    return area

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalRectangle(matrix=matrix))