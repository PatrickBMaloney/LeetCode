# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example 1:


# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:

# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 100

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        memo = {}
        return self.minPathHelper(0, 0, memo)
        
    def minPathHelper(self, row, col, memo):
        key = str(row) + ", "  + str(col)
        if key in memo:
            return memo[key]
        if row == len(self.grid) - 1 and col == len(self.grid[row]) - 1:
            memo[key] =  self.grid[row][col]
            return memo[key]
        if row < len(self.grid) - 1 and col < len(self.grid[row]) - 1:
            right = self.minPathHelper(row, col + 1, memo)
            down = self.minPathHelper(row + 1, col, memo)
            memo[key] = self.grid[row][col] + min(right, down)
            return memo[key]
        if row < len(self.grid) - 1 and col >= len(self.grid[row]) - 1:
            memo[key] =  self.grid[row][col] + self.minPathHelper(row + 1, col, memo)
            return memo[key]
        if row >= len(self.grid) - 1 and col < len(self.grid[row]) - 1:
            memo[key] =  self.grid[row][col] + self.minPathHelper(row, col + 1, memo)
            return memo[key]