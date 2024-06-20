#
# @lc app=leetcode id=709 lang=python
#
# [709] To Lower Case
#

# @lc code=start
class Solution(object):
    def toLowerCase(self, s):
        for char in s:
            char = char.lower()

        return s

# @lc code=end
