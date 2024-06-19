#
# @lc app=leetcode id=1920 lang=python
#
# [1920] Build Array from Permutation
#

# @lc code=start
class Solution(object):
    def buildArray(self, nums):
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans

# @lc code=end
