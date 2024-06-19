#
# @lc app=leetcode id=3146 lang=python
#
# [3146] Permutation Difference between Two Strings
#

# @lc code=start
class Solution(object):
    def findPermutationDifference(self, s, t):
        ans = 0
        for i in range(len(s)):

            # @lc code=end
