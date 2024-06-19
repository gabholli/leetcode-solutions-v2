#
# @lc app=leetcode id=2942 lang=python
#
# [2942] Find Words Containing Character
#

# @lc code=start
class Solution(object):
    def findWordsContaining(self, words, x):
        indices = []
        for i in range(len(words)):
            if x in words[i]:
                indices.append(i)

        return indices

    # O(n^2) T, O(1) S

# @lc code=end
