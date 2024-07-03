#
# @lc app=leetcode id=621 lang=python
#
# [621] Task Scheduler
#

# @lc code=start

from heapq import *


class Solution(object):
    def leastInterval(self, tasks, n):
        interval_count = 0

        freq = {}
        max_heap = []

        for char in tasks:
            freq[char] = freq.get(char, 0) + 1

        for char, f in freq.items():
            heappush(max_heap, (-f, char))

        while max_heap:
            waitlist = []
            k = n + 1
            while k > 0 and max_heap:
                interval_count += 1
                f, char = heappop(max_heap)
                if -f > 1:
                    waitlist.append((f + 1, char))
                k -= 1

            for f, char in waitlist:
                heappush(max_heap, (f, char))

            if max_heap:
                interval_count += k

        return interval_count

    # O(nlog(n)) T, O(n) S


# @lc code=end
