#
# @lc app=leetcode id=1207 lang=python
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
class Solution(object):
    def uniqueOccurrences(self, arr):
        unique = set()
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        for value in freq.values():
            unique.add(value)

        return len(unique) == len(freq)

    # O(n) T, O(n) S

# @lc code=end
