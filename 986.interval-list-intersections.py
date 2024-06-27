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
        result = []
        firstList.sort()
        secondList.sort()
        firstList = [Interval(start, end) for start, end in firstList]
        secondList = [Interval(start, end) for start, end in secondList]

        i, j = 0, 0

        while i < len(firstList) and j < len(secondList):
            a_overlaps_b = firstList[i].start >= secondList[j].start and \
                firstList[i].start <= secondList[j].end
            b_overlaps_a = secondList[j].start >= firstList[i].start and \
                secondList[j].start <= firstList[i].end

            if a_overlaps_b or b_overlaps_a:
                result.append([max(firstList[i].start, secondList[j].start),
                              min(firstList[i].end, secondList[j].end)])

            if firstList[i].end < secondList[j].end:
                i += 1
            else:
                j += 1

        return result

    # O(n) T, O(n) S

# @lc code=end
