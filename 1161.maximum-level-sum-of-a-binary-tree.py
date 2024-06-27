#
# @lc app=leetcode id=1161 lang=python
#
# [1161] Maximum Level Sum of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        if root is None:
            return root

        level = 0
        max_level_sum = 0
        queue = [root]
        current_level_sum = 0
        while queue:
            level_size = len(queue)

            level_sum = 0.0
            for _ in range(level_size):
                current_node = queue.pop(0)

                current_level_sum += current_node.val

                level += 1

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            max_level_sum = max(max_level_sum, current_level_sum)


# @lc code=end
