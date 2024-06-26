#
# @lc app=leetcode id=2351 lang=python
#
# [2351] First Letter to Appear Twice
#

# @lc code=start
class Solution(object):
    def repeatedCharacter(self, s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for char in s:
            if freq[char] == 2:
                return char

        return -1
# @lc code=end
