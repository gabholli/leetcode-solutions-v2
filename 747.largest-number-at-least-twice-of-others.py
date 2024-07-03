#
# @lc app=leetcode id=747 lang=python
#
# [747] Largest Number At Least Twice of Others
#

# @lc code=start
class Solution(object):
    def dominantIndex(self, nums):
        largest = max(nums)

        for i, num in enumerate(nums):
            if largest / num >= 2:
                print(i)

        return -1

    # O(n) T, O(1) S

# @lc code=end
