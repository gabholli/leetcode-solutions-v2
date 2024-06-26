#
# @lc app=leetcode id=637 lang=python
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        if root is None:
            return root

        queue = [root]

        result = []

        while queue:
            level_size = len(queue)

            level_sum = 0.0

            for _ in range(level_size):
                current_node = queue.pop(0)

                level_sum += current_node.val

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            result.append(level_sum / level_size)

        return result

    # O(n) T, O(n) S

# @lc code=end
