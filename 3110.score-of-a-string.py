#
# @lc app=leetcode id=3110 lang=python
#
# [3110] Score of a String
#

# @lc code=start
class Solution(object):
    def scoreOfString(self, s):
        result = list(s)
        score = 0

        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))

        return score

    # O(n) T, O(1) S

# @lc code=end
