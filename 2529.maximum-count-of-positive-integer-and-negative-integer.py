#
# @lc app=leetcode id=2529 lang=python
#
# [2529] Maximum Count of Positive Integer and Negative Integer
#

# @lc code=start
class Solution(object):
    def maximumCount(self, nums):
        positive_count, negative_count = 0, 0

        for num in nums:
            if num > 0:
                positive_count += 1
            elif num < 0:
                negative_count += 1

        return max(positive_count, negative_count)

    # O(n) T, O(1) S
# @lc code=end
