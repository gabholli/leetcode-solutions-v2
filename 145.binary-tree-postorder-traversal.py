#
# @lc app=leetcode id=145 lang=python
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        return self.helper(root, [])

    def helper(self, node, array):
        if node:
            self.helper(node.left, array)
            self.helper(node.right, array)
            array.append(node.val)

        return array

    # O(n) T, O(n) S

# @lc code=end
