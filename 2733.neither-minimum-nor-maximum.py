#
# @lc app=leetcode id=2733 lang=python
#
# [2733] Neither Minimum nor Maximum
#

# @lc code=start
class Solution(object):
    def findNonMinOrMax(self, nums):
        min_num = min(nums)
        max_num = max(nums)

        for num in nums:
            if num != min_num and num != max_num:
                return num

        return -1

        # O(n) T, O(1) S

# @lc code=end
