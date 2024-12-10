#
# @lc app=leetcode id=643 lang=python
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution(object):
    def findMaxAverage(self, nums, k):
        window_start, window_sum = 0, 0
        max_avg = float("-inf")
        length = float("inf")

        for window_end in range(len(nums)):
            window_sum += nums[window_end]
            if window_end == k:
                window_sum -= nums[window_start]
                length = window_end - window_start + 1
                max_avg = max(max_avg, window_sum / length)
                window_start += 1

        return max_avg

# @lc code=end
