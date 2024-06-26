#
# @lc app=leetcode id=977 lang=python
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution(object):
    def sortedSquares(self, nums):
        left, right = 0, len(nums) - 1
        squares = [0] * len(nums)
        next_highest_idx = len(nums) - 1

        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]

            if left_square > right_square:
                squares[next_highest_idx] = left_square
                left += 1
            else:
                squares[next_highest_idx] = right_square
                right -= 1

            next_highest_idx -= 1

        return squares

    # O(n) T, O(n) S

# @lc code=end
