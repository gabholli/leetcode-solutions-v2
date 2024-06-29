#
# @lc app=leetcode id=1287 lang=python
#
# [1287] Element Appearing More Than 25% In Sorted Array
#

# @lc code=start
class Solution(object):
    def findSpecialInteger(self, arr):
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        for key, value in freq.items():
            print(value / len(arr))

# @lc code=end
