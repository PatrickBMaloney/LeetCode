# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Follow up: Could you do this in one pass?

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque 
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next:
            return head.next
        
        nth = cur = head
        count = 1
        while cur.next:
            if count == n + 1:
                nth = nth.next
            else:
                count += 1
            cur = cur.next
        
        if count < n + 1:
            return head.next
        
        nth.next = nth.next.next
        return head