#
# @lc app=leetcode id=173 lang=python
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        self.stack = list()
        self.traverse_left(root)

    def next(self):
        temp = self.stack.pop()
        self.traverse_left(temp.right)
        return temp.val

    def hasNext(self):
        return self.stack

    def traverse_left(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left

    # O(n) T, O(n) S

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
