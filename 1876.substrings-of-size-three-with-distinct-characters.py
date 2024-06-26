#
# @lc app=leetcode id=1876 lang=python
#
# [1876] Substrings of Size Three with Distinct Characters
#

# @lc code=start
class Solution(object):
    def countGoodSubstrings(self, s):
        freq = {}
        temp = []
        window_start = 0

        for window_end in range(len(s)):
            right = s[window_end]
            if right not in freq:
                freq[right] = 0
            freq[right] += 1

            while len(freq) > 3:
                left = s[window_start]

# @lc code=end
