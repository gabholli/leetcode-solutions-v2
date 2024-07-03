#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        numbers = {}

        for i, num in enumerate(nums):
            potential_match = target - num
            if potential_match in numbers:
                return [numbers[potential_match], i]
            else:
                numbers[num] = i

        return [-1, -1]

    # O(n) T, o(n) S
# @lc code=end
