# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

# Example 1:

# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.

from collections import deque


# Direction vectors
dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]

class Solution:
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    
        queue = deque()
        
        maxSize = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    queue.append((row, col))
                    size = 1
                    while len(queue) != 0:
                        row, col = queue.popleft()
                        # Go to the adjacent cells
                        # for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            
                        for i in range(4):
                            adjx = row + dRow[i]
                            adjy = col + dCol[i]
                            if adjx >= 0 and adjy >= 0 and adjx < len(grid) and adjy < len(grid[row]):
                                if grid[adjx][adjy] == 1:
                                    grid[adjx][adjy] = 0
                                    queue.append((adjx, adjy))
                                    size += 1
                    if size > maxSize:
                        maxSize = size
        return maxSize