#
# @lc app=leetcode id=986 lang=python
#
# [986] Interval List Intersections
#

# @lc code=start

class Interval:

    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution(object):
    def intervalIntersection(self, firstList, secondList):

        # @lc code=end
