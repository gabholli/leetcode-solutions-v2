#
# @lc app=leetcode id=1662 lang=python
#
# [1662] Check If Two String Arrays are Equivalent
#

# @lc code=start
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        return ''.join(word1) == ''.join(word2)

    # O(m + n) T, O(m + n) S

# @lc code=end
