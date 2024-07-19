#
# @lc app=leetcode id=3173 lang=python
#
# [3173] Bitwise OR of Adjacent Elements
#

# @lc code=start
class Solution(object):
    def orArray(self, nums):
        answer = [i for i in range(len(nums) - 1)]

        for i in range(1, len(nums)):
            answer[i] = nums[i] ^ nums[i - 1]

        return answer

# @lc code=end
