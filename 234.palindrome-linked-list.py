#
# @lc app=leetcode id=234 lang=python
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if head is None:
            return head

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = self.reverse(slow)

        while head and second_half:
            if head.val != second_half.val:
                break

            head = head.next
            second_half = second_half.next

        if head is None or second_half is None:
            return True

        return False

    def reverse(self, head):
        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

    # O(n) T, O(1) S


# @lc code=end
