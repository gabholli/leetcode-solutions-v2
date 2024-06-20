#
# @lc app=leetcode id=2859 lang=python
#
# [2859] Sum of Values at Indices With K Set Bits
#

# @lc code=start
class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        n1xn2 = 0

        for num in nums:
            n1xn2 ^= num

        rightmost_bit = 1
        while rightmost_bit & n1xn2 == 0:
            rightmost_bit = rightmost_bit << 1

        ans = 0
        num1 = 0

        for num in nums:
            if num & rightmost_bit == 0:
                num1 ^= num
                ans += 1

        return ans

# @lc code=end
