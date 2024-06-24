#
# @lc app=leetcode id=226 lang=python
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if root is None:
            return root

        queue = [root]

        while queue:
            current_node = queue.pop(0)

            if current_node is None:
                continue

            current_node.left, current_node.right = current_node.right, current_node.left

            queue.append(current_node.left)
            queue.append(current_node.right)

        return root

    # O(n) T, O(n) S

# @lc code=end
