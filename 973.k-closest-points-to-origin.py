#
# @lc app=leetcode id=973 lang=python
#
# [973] K Closest Points to Origin
#

# @lc code=start

from heapq import *


class Solution(object):
    def kClosest(self, points, k):

        # O(nlog(k)) T, O(k) S

        # @lc code=end
