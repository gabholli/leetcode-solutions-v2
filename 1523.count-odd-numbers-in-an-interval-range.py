#
# @lc app=leetcode id=1523 lang=python
#
# [1523] Count Odd Numbers in an Interval Range
#

# @lc code=start
class Solution(object):
    def countOdds(self, low, high):
        count = 0
        for i in range(low, high + 1):
            if i % 2 == 1:
                count += 1

        return count

    # O(n) T O(1) S

# @lc code=end
