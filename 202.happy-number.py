#
# @lc app=leetcode id=202 lang=python
#
# [202] Happy Number
#

# @lc code=start
class Solution(object):
    def isHappy(self, n):
        slow, fast = n, n
        while True:
            slow = self.helper(slow)
            fast = self.helper(self.helper(fast))

            if slow == fast:
                break

        return slow == 1

    def helper(self, num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10

        return total

    # O(log(n)) T, O(1) S

# @lc code=end
