#
# @lc app=leetcode id=2487 lang=python
#
# [2487] Remove Nodes From Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        stack = []
        cur = head

        while cur:
            while stack and stack[-1].val < cur.val:
                stack.pop()
            if stack:
                stack[-1].next = cur
            stack.append(cur)
            cur = cur.next

        return stack[0] if stack else None

    # O(n) T, O(n) S

# @lc code=end
