# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 0 <= n <= 3 * 104
# 0 <= height[i] <= 105

class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        right = []
        
        lmax = 0
        for x in height:
            lmax = max(x,lmax)
            left.append(lmax)
        
        rmax = 0
        for x in height[::-1]:
            rmax = max(x,rmax)
            right.append(rmax)
        right = right[::-1]
        res = 0
        for x in range(1,len(height)-1):
            val = min(left[x],right[x]) - height[x]
            res += max(val,0)
        
        return res