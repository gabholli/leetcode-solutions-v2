#
# @lc app=leetcode id=1486 lang=python
#
# [1486] XOR Operation in an Array
#

# @lc code=start
class Solution(object):
    def xorOperation(self, n, start):
        running_xor = 0
        nums = []
        for i in range(n):
            nums.append(start + 2 * i)

        for num in nums:
            running_xor ^= num

        return running_xor

    # O(n) T, O(n) S

# @lc code=end
