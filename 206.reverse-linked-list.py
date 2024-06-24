#
# @lc app=leetcode id=206 lang=python
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev

    # O(n) T, O(1) S

# @lc code=end
