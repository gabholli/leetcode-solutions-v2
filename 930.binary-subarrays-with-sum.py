#
# @lc app=leetcode id=930 lang=python
#
# [930] Binary Subarrays With Sum
#

# @lc code=start
class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        count = 0  # Initialize count of subarrays
        cum_map = {0: 1}
        cum_sum = 0

        for num in nums:
            cum_sum += num

            if cum_sum - goal in cum_map:
                count += cum_map.get(cum_sum - goal, 0)

            if cum_sum in cum_map:
                cum_map[cum_sum] += 1
            else:
                cum_map[cum_sum] = 1

        return count
        # @lc code=end
