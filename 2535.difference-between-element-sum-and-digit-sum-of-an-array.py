#
# @lc app=leetcode id=2535 lang=python
#
# [2535] Difference Between Element Sum and Digit Sum of an Array
#

# @lc code=start
class Solution(object):
    def differenceOfSum(self, nums):
        element_sum = sum(nums)
        digit_sum = 0

        for i in range(len(nums) - 1):
            digit_sum += nums[i] + nums[i + 1]
        print(element_sum)
        print(digit_sum)
        return abs(element_sum - digit_sum)

    # O(n) T, O(1) S

# @lc code=end
