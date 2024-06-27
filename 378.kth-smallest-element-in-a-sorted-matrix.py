#
# @lc app=leetcode id=378 lang=python
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start

from heapq import *


class Solution(object):
    def kthSmallest(self, matrix, k):
        min_heap = []
        number = 0
        number_count = 0

        for i in range(0, min(k, len(matrix))):
            heappush(min_heap, (matrix[i][0], 0, matrix[i]))

        while min_heap:
            number, i, arr = heappop(min_heap)
            number_count += 1
            if number_count == k:
                break
            if len(arr) > i + 1:
                heappush(min_heap, (arr[i + 1], i + 1, arr))

        return number

    # O(nlog(k)) T, O(k) S

# @lc code=end
