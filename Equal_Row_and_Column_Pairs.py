'''
2352. Equal Row and Column Pairs

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Example 1:

Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:

Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
'''

def equalPairs(grid):
    
    cols_matrix = []
    
    for i in range(len(grid)):
        temp = []
        for j in range(len(grid)):
            temp.append(grid[j][i])
        cols_matrix.append(temp)

    
    result = 0
    counter = {}
    for i in grid:
        if str(i) not in counter:
            counter[str(i)] = 1
        else:
            counter[str(i)] += 1
    for i in cols_matrix:
        if str(i) in counter:
            result += counter[str(i)]

    return result

#Sample Input.