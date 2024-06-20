#
# @lc app=leetcode id=2520 lang=python
#
# [2520] Count the Digits That Divide a Number
#

# @lc code=start
class Solution(object):
    def countDigits(self, num):
        digits_count = 0

        for i in range(1, num + 1):
            if num % i == 0:
                digits_count += 1

        return digits_count

    # O(n) T, O(1) S

# @lc code=end
