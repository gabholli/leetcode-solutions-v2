#
# @lc app=leetcode id=2363 lang=python
#
# [2363] Merge Similar Items
#

# @lc code=start

from collections import defaultdict


class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        merged = defaultdict(int)

        for item, value in items1:
            merged[item] += value

        for item, value in items2:
            merged[item] += value

        return [[item, value] for item, value in merged.items()]


# @lc code=end
