#
# @lc app=leetcode id=1512 lang=python
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution(object):
    def numIdenticalPairs(self, nums):
        pairs = 0
        numbers = {}
        for num in nums:
            numbers[num] = numbers.get(num, 0) + 1
            pairs += numbers[num] - 1

        return pairs
    # O(n) T, O(n) S


# @lc code=end
