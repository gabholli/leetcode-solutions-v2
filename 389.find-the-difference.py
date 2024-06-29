#
# @lc app=leetcode id=389 lang=python
#
# [389] Find the Difference
#

# @lc code=start
class Solution(object):
    def findTheDifference(self, s, t):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for char in t:
            if char not in freq or freq[char] == 0:
                return char
            else:
                freq[char] -= 1

# @lc code=end
