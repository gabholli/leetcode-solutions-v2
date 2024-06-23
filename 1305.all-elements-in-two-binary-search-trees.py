#
# @lc app=leetcode id=1305 lang=python
#
# [1305] All Elements in Two Binary Search Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        self.traverse_root1(root1)
        return self.helper(root1, root2, [])

    def traverse_root1(self, root1):
        if root1 is None:
            return

        output = []

        left_subtree = self.traverse_root1(root1.left.val)
        right_subtree = self.traverse_root1(root1.right)

        output.append(left_subtree.val)
        print(output)
# @lc code=end
