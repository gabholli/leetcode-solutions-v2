#
# @lc app=leetcode id=1009 lang=python
#
# [1009] Complement of Base 10 Integer
#

# @lc code=start
class Solution(object):
    def bitwiseComplement(self, n):
        if n == 0:
            return 1
        bits = 0

        num = n
        while num > 0:
            bits += 1
            num = num >> 1

        all_bits_set = pow(2, bits) - 1

        return n ^ all_bits_set

    # O(n) T, O(1) S

# @lc code=end
