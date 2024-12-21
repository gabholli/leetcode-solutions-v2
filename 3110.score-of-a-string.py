#
# @lc app=leetcode id=3110 lang=python
#
# [3110] Score of a String
#

# @lc code=start
class Solution(object):
    def scoreOfString(self, s):
        score = 0

        for i in range(1, len(s)):
            score += abs(ord(s[i]) - ord(s[i - 1]))

        return score

    # O(n) T< O(1) S
        # @lc code=end
