#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#

# @lc code=start

from collections import defaultdict


class Solution(object):
    def longestPalindrome(self, s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        first_half, middle = [], ""

        for i in range(len(s) - 1, -1, -1):
            if freq[i] % 2 != 0 and middle == "":
                middle = i

# @lc code=end
