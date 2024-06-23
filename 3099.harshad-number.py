#
# @lc app=leetcode id=3099 lang=python
#
# [3099] Harshad Number
#

# @lc code=start
class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        running_sum = 0
        for digit in str(x):
            running_sum += int(digit)
        if x % running_sum == 0:
            return running_sum
        return -1

        # O(n) T, O(1) S


# @lc code=end
