#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start

from heapq import *


class Solution(object):
    def topKFrequent(self, nums, k):
        min_heap = []
        freq = {}
        result = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, f in freq.items():
            heappush(min_heap, (f, num))
            if len(min_heap) > k:
                heappop(min_heap)

        while min_heap:
            result.append(heappop(min_heap)[1])

        return result

    # O(nlog(k)) T, O(n + k) S

# @lc code=end
