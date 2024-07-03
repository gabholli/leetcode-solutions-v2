#
# @lc app=leetcode id=2404 lang=python
#
# [2404] Most Frequent Even Element
#

# @lc code=start
class Solution(object):
    def mostFrequentEven(self, nums):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        max_num = 0

        most_frequent = []
        for key, value in freq.items():
            max_num = max(max_num, value)


# @lc code=end
