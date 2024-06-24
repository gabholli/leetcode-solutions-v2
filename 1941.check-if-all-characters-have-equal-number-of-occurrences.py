#
# @lc app=leetcode id=1941 lang=python
#
# [1941] Check if All Characters Have Equal Number of Occurrences
#

# @lc code=start
class Solution(object):
    def areOccurrencesEqual(self, s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        values_list = []
        for value in freq.values():
            values_list.append(value)

        for i in range(len(values_list)):
            if values_list[0] != values_list[i]:
                return False

        return True

    # O(n) T, O(n) S

# @lc code=end
