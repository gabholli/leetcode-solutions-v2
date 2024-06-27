#
# @lc app=leetcode id=852 lang=python
#
# [852] Peak Index in a Mountain Array
#

# @lc code=start
class Solution(object):
    def peakIndexInMountainArray(self, arr):
        start, end = 0, len(arr) - 1
        is_ascending = arr[start] < arr[end]

        while start < end:
            mid = start + (end - start) // 2

            if is_ascending:
                if arr[start] < arr[mid]:
                    start = mid + 1

            return start + 1

        # O(log(n)) T, O(1) S


# @lc code=end
