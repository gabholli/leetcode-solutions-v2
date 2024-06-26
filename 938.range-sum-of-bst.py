#
# @lc app=leetcode id=938 lang=python
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        return self.helper(root, low, high)

    def helper(self, current_node, low, high):
        if current_node is None:
            return 0

        total = 0

        if current_node.val >= low and current_node.val <= high:
            total += current_node.val

        total += self.helper(current_node.left, low, high)
        total += self.helper(current_node.right, low, high)

        return total
    # O(n) T, O(n) S

# @lc code=end
