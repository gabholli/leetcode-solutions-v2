#
# @lc app=leetcode id=472 lang=python
#
# [472] Concatenated Words
#

# @lc code=start
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        if len(words) == 0 or len(words[0]) == 0:
            return []

        result = []

        freq = {}

        for word in words:
            if word not in freq:
                freq[word] = 0
            freq[word] += 1

        for
# @lc code=end
