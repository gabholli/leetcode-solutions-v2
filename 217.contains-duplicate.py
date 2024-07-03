#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        numbers = set()

        for num in nums:
            if num in numbers:
                return True
            numbers.add(num)

        return False

    # O(n) T, O(n) S

# @lc code=end
