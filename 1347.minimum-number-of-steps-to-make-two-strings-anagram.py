#
# @lc app=leetcode id=1347 lang=python
#
# [1347] Minimum Number of Steps to Make Two Strings Anagram
#

# @lc code=start
class Solution(object):
    def minSteps(self, s, t):
        letters = {}
        for char in s:
            letters[char] = letters.get(char, 0) + 1

        print(letters)

# @lc code=end
