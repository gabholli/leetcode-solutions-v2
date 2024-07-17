#
# @lc app=leetcode id=2824 lang=python
#
# [2824] Count Pairs Whose Sum is Less than Target
#

# @lc code=start
class Solution(object):
    def countPairs(self, nums, target):
        nums.sort()
        l, r = 0, len(nums) - 1
        count = 0

        while l < r:
            if nums[l] + nums[r] < target:
                count += r - l
                l += 1
            else:
                r -= 1

        return count

    # O(nlog(n)) T, O(n) S

        # @lc code=end
