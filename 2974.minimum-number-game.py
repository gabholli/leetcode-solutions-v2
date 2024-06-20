#
# @lc app=leetcode id=2974 lang=python
#
# [2974] Minimum Number Game
#

# @lc code=start
class Solution(object):
    def numberGame(self, nums):
        stack = []
        arr = []
        for num in nums:
            stack.append(min(nums))
            nums.remove(stack.pop())
            arr.append(stack.pop())

        return arr

# @lc code=end
