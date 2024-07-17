#
# @lc app=leetcode id=692 lang=python
#
# [692] Top K Frequent Words
#

# @lc code=start
from heapq import *


class Solution(object):
    def topKFrequent(self, words, k):
        min_heap = []
        freq = {}
        result = []

        for word in words:
            freq[word] = freq.get(word, 0) + 1

        for word, f in freq.items():
            heappush(min_heap, (f, word))
            if len(min_heap) > k:
                heappop(min_heap)

        while min_heap:
            result.append(heappop(min_heap)[1])

        return result

    # O(nlog(k)) T, O(n + k) S
# @lc code=end
