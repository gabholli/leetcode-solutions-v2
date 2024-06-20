#
# @lc app=leetcode id=1816 lang=python
#
# [1816] Truncate Sentence
#

# @lc code=start
class Solution(object):
    def truncateSentence(self, s, k):
        new_words = []
        for i, word in enumerate(s):
            if i <= k:
                new_words.append(word)
        return ''.join(new_words)

    # O(n) T, O(n) S

# @lc code=end
