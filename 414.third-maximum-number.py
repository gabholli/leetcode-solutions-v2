#
# @lc app=leetcode id=414 lang=python
#
# [414] Third Maximum Number
#

# @lc code=start

from heapq import *


class Solution(object):
    def thirdMax(self, nums):
        max_heap = []

        for num in nums:
            heappush(max_heap, -num)

        for num in nums:
            if -num > max_heap[0]:
                heappop(max_heap)
                heappush(max_heap, -num)

        return -max_heap[2] if -max_heap[2] else -max_heap[0]

# @lc code=end
