#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        zeroes = 1
        i = 0

        while i < len(nums - 1):
            if nums[zeroes - 1] != nums[i]:
                nums[zeroes + 1] = nums[i]
                zeroes += 1
            i += 1

        re

# @lc code=end
