#
# @lc app=leetcode id=973 lang=python
#
# [973] K Closest Points to Origin
#

# @lc code=start

from heapq import *


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    def distance_from_origin(self):
        return self.x ** 2 + self.y ** 2


class Solution(object):
    def kClosest(self, points, k):
        points = [Point(x, y) for x, y in points]
        result = []

        max_heap = []

        for i in range(k):
            heappush(max_heap, (-points[i].distance_from_origin(), points[i]))

        for i in range(k, len(points)):
            distance = points[i].distance_from_origin()

            if distance < -max_heap[0][0]:
                heappop(max_heap)
                heappush(max_heap, (-distance, points[i]))

        while max_heap:
            result.append(heappop(max_heap)[1])

        return [[point.x, point.y] for point in result]

    # O(nlog(k)) T, O(k) S

# @lc code=end
