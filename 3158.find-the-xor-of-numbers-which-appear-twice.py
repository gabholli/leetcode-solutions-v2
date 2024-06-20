#
# @lc app=leetcode id=3158 lang=python
#
# [3158] Find the XOR of Numbers Which Appear Twice
#

# @lc code=start
class Solution(object):
    def duplicateNumbersXOR(self, nums):

    def appears_twice(self, nums):
        n1xn2 = 0

        for num in nums:
            n1xn2 ^= num

        rightmost = 1

        while rightmost & n1xn2 == 0:
            rightmost = rightmost << 1

        num1, num2 = 0, 0

        for num in

# @lc code=end
