#
# @lc app=leetcode id=3190 lang=python
#
# [3190] Find Minimum Operations to Make All Elements Divisible by Three
#

# @lc code=start
class Solution(object):
    def minimumOperations(self, nums):
        count = 0
        for num in nums:
            if num % 3 != 0:
                count += 1
        return count

    # O(n) T, O(1) S
# @lc code=end
