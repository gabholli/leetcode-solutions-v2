#
# @lc app=leetcode id=1832 lang=python
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start
class Solution(object):
    def checkIfPangram(self, sentence):
        letters = set()
        for char in sentence.lower():
            letters.add(char)

        return len(letters) == 26

    # O(n) T, O(1) S

# @lc code=end
