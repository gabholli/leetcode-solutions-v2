#
# @lc app=leetcode id=2894 lang=python
#
# [2894] Divisible and Non-divisible Sums Difference
#

# @lc code=start
class Solution(object):
    def differenceOfSums(self, n, m):
        num1, num2 = 0, 0
        for i in range(1, n + 1):
            if i % m != 0:
                num1 += i

        for i in range(1, n + 1):
            if i % m == 0:
                num2 += i

        return num1 - num2

    # O(n) T, O(1) S
# @lc code=end
