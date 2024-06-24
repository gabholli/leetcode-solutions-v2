#
# @lc app=leetcode id=104 lang=python
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0

        queue = [root]
        max_depth = 0

        while queue:
            level_size = len(queue)

            max_depth += 1

            for _ in range(level_size):
                current_node = queue.pop(0)

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

        return max_depth

    # O(n) T, O(n) S

# @lc code=end
