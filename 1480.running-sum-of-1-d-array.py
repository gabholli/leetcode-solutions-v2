#
# @lc app=leetcode id=1480 lang=python
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution(object):
    def runningSum(self, nums):
        cum_sum = 0
        result = [0] * len(nums)

        for i in range(len(nums)):
            cum_sum += nums[i]

            result[i] = cum_sum

        return result

    # O(n) T, O(n) S


# @lc code=end
