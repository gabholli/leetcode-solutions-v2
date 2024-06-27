#
# @lc app=leetcode id=1394 lang=python
#
# [1394] Find Lucky Integer in an Array
#

# @lc code=start
class Solution(object):
    def findLucky(self, arr):
        freq = {}
        max_num = 0
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        for key, value in freq.items():
            if key == value:
                max_num = max(max_num, key)

        if max_num > 0:
            return max_num

        return -1

    # O(n) T, O(n) S

# @lc code=end
