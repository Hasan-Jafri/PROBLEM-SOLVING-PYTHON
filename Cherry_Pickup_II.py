'''
1463. Cherry Pickup II

You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

You have two robots that can collect cherries for you:

Robot #1 is located at the top-left corner (0, 0), and
Robot #2 is located at the top-right corner (0, cols - 1).
Return the maximum number of cherries collection using both robots by following the rules below:

From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
When both robots stay in the same cell, only one takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in grid.
 

Example 1:


Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
Output: 24
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
Total of cherries: 12 + 12 = 24.
Example 2:


Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
Output: 28
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
Total of cherries: 17 + 11 = 28.

Constraints:

rows == grid.length
cols == grid[i].length
2 <= rows, cols <= 70
0 <= grid[i][j] <= 100
'''
# Dynamic Array to store result.
dp = []
# Array to assist in next step i.e a Robot can take any of the three steps at a time.
choice = [-1,0,1]
# This function checks every possibility for the path giving us the optimal answer with no overlapping substructure.
def helper(grid,m,n,r,c1,c2):
    # m is the no. of rows, n is no. of columns, r is the current row while c1 and c2 are columns for Robot 1 and 2.
    if m == r:
        return 0
    # To avoid overlappping we use the existing value to calculate further.
    if dp[r][c1][c2] != -1:
        return dp[r][c1][c2]
    # If no value or base case found we move towards calculation.
    cherries = 0
    if c1 == c2:
        cherries = grid[r][c1]
    else:
        cherries = grid[r][c1] + grid[r][c2]
    next_ = 0
    # This loop basically checks for all possible paths for each Robot checing every path.
    # Robots can move simultaneously that is why 9 moves are possible at most.
    for i in range(3):
        for j in range(3):
            nc1 = c1 + choice[i] # Used assist array for move.
            nc2 = c2 + choice[j]
            if nc1 >= 0 and nc1 < n and nc2 >= 0 and nc2 < n:
                next_ = max(next_, helper(grid,m,n,r+1,nc1,nc2)) # Recursive call to checks for every combination after this.
    dp[r][c1][c2] = next_ + cherries
    return dp[r][c1][c2] # At the end returns the result from the array.
def cherryPickup(grid) -> int: # This function just created the array and calls the helper function and returns the answer.
    for i in range(len(grid)):
        temp = []
        for j in range(len(grid[0])):
            temp2 = []
            for k in range(len(grid[0])):
                temp2.append(-1)
            temp.append(temp2)
        dp.append(temp)
    m = len(grid)
    n = len(grid[0])
    return helper(grid,m,n,0,0,n-1)

# Sample Input
grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
print(cherryPickup(grid = grid))