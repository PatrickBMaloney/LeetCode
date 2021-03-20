# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []
 

# Constraints:

# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = []
        for i in range(len(nums)):
            diffs = set()
            if i>0 and nums[i] == nums[i-1]:
                continue
            j=i+1
            while j<len(nums):
                if (-nums[j] - nums[i]) in diffs:
                    result.append([nums[j],nums[i],-nums[i]-nums[j]])
                    while j<len(nums)-1 and nums[j]==nums[j+1]:
                        j+=1
                diffs.add(nums[j])
                j+=1
        
        return result