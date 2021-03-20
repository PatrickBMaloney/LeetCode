# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

# Example 1:

# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
# Example 2:

# Input: triangle = [[-10]]
# Output: -10
 

# Constraints:

# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -104 <= triangle[i][j] <= 104

import copy
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        i = len(triangle) - 1
        while i > 0:
            for j in range(len(triangle[i-1])):
                triangle[i-1][j] = min(triangle[i][j], triangle[i][j+1]) + triangle[i-1][j]
            i -= 1
        return triangle[0][0]
                
                
        
        
        
        
#         self.triangle = triangle
#         memo = {}
#         return self.helpMinTriangle(0, 0, memo)
        
#     def helpMinTriangle(self, row, col, memo):
#         key = str(row) + ", " + str(col)
#         if key in memo:
#             return memo[key]
#         if row >= len(self.triangle):
#             return 0
#         left = self.helpMinTriangle(row + 1, col, memo)
#         right = self.helpMinTriangle(row + 1, col + 1, memo)
        
#         memo[key] = self.triangle[row][col] + min(left, right)
#         return memo[key]