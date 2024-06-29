#
# @lc app=leetcode id=387 lang=python
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution(object):
    def firstUniqChar(self, s):
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for i, char in enumerate(s):
            if freq[char] == 1:
                return i

        return -1

    # O(n) T, O(1) S

# @lc code=end
