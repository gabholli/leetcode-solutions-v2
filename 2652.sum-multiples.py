#
# @lc app=leetcode id=2652 lang=python
#
# [2652] Sum Multiples
#

# @lc code=start
class Solution(object):
    def sumOfMultiples(self, n):
        int_sum = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                int_sum += i

        return int_sum

    # O(n) T, O(1) S

# @lc code=end
