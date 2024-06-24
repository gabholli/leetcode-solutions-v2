#
# @lc app=leetcode id=94 lang=python
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        return self.helper(root, [])

    def helper(self, current_node, array):
        if current_node:
            self.helper(current_node.left, array)
            array.append(current_node.val)
            self.helper(current_node.right, array)
        return array

    # O(n) T, O(n) S
# @lc code=end
