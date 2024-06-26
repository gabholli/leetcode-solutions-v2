#
# @lc app=leetcode id=2057 lang=python
#
# [2057] Smallest Index With Equal Value
#

# @lc code=start
class Solution(object):
    def smallestEqual(self, nums):
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i

        return -1

    # O(n) T, O(1) S
# @lc code=end
