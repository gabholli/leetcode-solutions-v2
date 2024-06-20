#
# @lc app=leetcode id=3065 lang=python
#
# [3065] Minimum Operations to Exceed Threshold Value I
#

# @lc code=start
class Solution(object):
    def minOperations(self, nums, k):
        count = 0
        for num in nums:
            if num < k:
                nums.remove(num)
                count += 1

        return count

# @lc code=end
