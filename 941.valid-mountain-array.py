#
# @lc app=leetcode id=941 lang=python
#
# [941] Valid Mountain Array
#

# @lc code=start
class Solution(object):
    def validMountainArray(self, arr):
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                return True
        return False

# @lc code=end
