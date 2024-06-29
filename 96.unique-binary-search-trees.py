#
# @lc app=leetcode id=96 lang=python
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution(object):
    def numTrees(self, n):
        if n <= 1:
            return 1

        count = 0

        for i in range(1, n + 1):
            left_subtree = self.numTrees(n - i)
            right_subtree = self.numTrees(i - 1)
            count += left_subtree * right_subtree

        return count

    # O(n * 2^n) T, O(2^n) S

# @lc code=end
