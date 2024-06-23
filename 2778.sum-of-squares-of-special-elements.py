#
# @lc app=leetcode id=2778 lang=python
#
# [2778] Sum of Squares of Special Elements
#

# @lc code=start
class Solution(object):
    def sumOfSquares(self, nums):
        n = len(nums)
        answer = 0
        for i in range(n):
            if n % i == 0:
                answer += nums[i] * nums[i]

        return answer

# @lc code=end
