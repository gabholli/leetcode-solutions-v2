#
# @lc app=leetcode id=1749 lang=python
#
# [1749] Maximum Absolute Sum of Any Subarray
#

# @lc code=start
class Solution(object):
    def maxAbsoluteSum(self, nums):
        window_start, window_sum, max_sum = 0, 0, 0

        for window_end in range(len(nums)):
            window_sum += nums[window_end]

# @lc code=end
