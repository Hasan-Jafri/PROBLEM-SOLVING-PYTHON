'''
931. Minimum Falling Path Sum

Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:


Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
Example 2:


Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100
'''

def minFallingPathSum(matrix):
    n = len(matrix)
    dp = []
    # First of all cloning matrix in dp.
    for i in matrix:
        temp = []
        for j in i:
            temp.append(j)
        dp.append(temp)
    # In this loop we perform all the calculations
    for i in range(1,n):
        for j in range(0,n):
            if j == 0:
                # Getting minimum calculations to get the minimum answer.
                dp[i][j] = min(dp[i-1][j],dp[i-1][j+1]) + matrix[i][j]
            elif j == n-1:
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j]) + matrix[i][j]
            else:
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1]) + matrix[i][j]
    # The answer is stored in the last row from which we get the minimum value out.
    return min(dp[n-1])

# Sample Input

matrix = [[2,1,3],[6,5,4],[7,8,9]]
print(minFallingPathSum(matrix = matrix))