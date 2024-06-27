#
# @lc app=leetcode id=476 lang=python
#
# [476] Number Complement
#

# @lc code=start
class Solution(object):
    def findComplement(self, num):
        bit_count = 0

        n = num

        while n > 0:
            bit_count += 1
            n = n >> 1

        all_bits_set = pow(2, bit_count) - 1

        return num ^ all_bits_set

    # O(n) T, O(1) S

# @lc code=end
