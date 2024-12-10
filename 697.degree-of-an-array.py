#
# @lc app=leetcode id=697 lang=python
#
# [697] Degree of an Array
#

# @lc code=start
class Solution(object):
    def findShortestSubArray(self, nums):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        degree = max(freq.values())

        min_length = float("inf")


# @lc code=end
