#
# @lc app=leetcode id=1672 lang=python
#
# [1672] Richest Customer Wealth
#

# @lc code=start
class Solution(object):
    def maximumWealth(self, accounts):
        total = 0
        for row in accounts:
            total = max(total, sum(row))

        return total

    # O(mn) T, O(1) S

# @lc code=end
