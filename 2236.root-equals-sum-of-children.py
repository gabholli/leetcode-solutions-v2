#
# @lc app=leetcode id=2236 lang=python
#
# [2236] Root Equals Sum of Children
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkTree(self, root):
        return root.val == root.left.val + root.right.val

    # O(1) T, O(1) S
# @lc code=end
