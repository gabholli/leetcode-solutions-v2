#
# @lc app=leetcode id=451 lang=python
#
# [451] Sort Characters By Frequency
#

# @lc code=start

from heapq import *


class Solution(object):
    def frequencySort(self, s):
        sorted_string = []
        freq = {}
        max_heap = []

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for char, f in freq.items():
            heappush(max_heap, (-f, char))

        while max_heap:
            f, char = heappop(max_heap)
            for _ in range(-f):
                sorted_string.append(char)

        return ''.join(sorted_string)

    # O(nlog(n)) T, O(n) S

# @lc code=end
