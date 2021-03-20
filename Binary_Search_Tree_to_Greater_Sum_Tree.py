# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

# As a reminder, a binary search tree is a tree that satisfies these constraints:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Note: This question is the same as 538: https://leetcode.com/problems/convert-bst-to-greater-tree/

 

# Example 1:


# Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# Example 2:

# Input: root = [0,null,1]
# Output: [1,null,1]
# Example 3:

# Input: root = [1,0,2]
# Output: [3,3,2]
# Example 4:

# Input: root = [3,2,4,1]
# Output: [7,9,4,10]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 100].
# 0 <= Node.val <= 100
# All the values in the tree are unique.
# root is guaranteed to be a valid binary search tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def helper(self, root: TreeNode, offset: int) -> TreeNode:
         if root:
            right = self.helper(root.right, offset)
            self.count += root.val
            total = root.val
            # if not right: 
            #     total += offset
            # if right and right.left:
            #     print(root.right.left)
            #     print(right.left.val)
            #     total += right.left.val
            # elif right:
            #     total += right.val
                
            # if right and not right.left:
            #     total += right.val
            # elif right and right.left:
            #     total += right.left.val
            
            newTree = TreeNode(self.count)
            # print(root.val)
            # print(newTree.val)
            newTree.right = right
            left = self.helper(root.left, total)
            
            newTree.left = left
            return newTree
         else: 
            return None
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            right = self.bstToGst(root.right)
            self.count += root.val
            newTree = TreeNode(self.count)
            # print(root.val)
            # print(newTree.val)
            newTree.right = right
            left = self.bstToGst(root.left)
            
            newTree.left = left
            return newTree
         # return self.helper(root, 0)
         # print(self.count)