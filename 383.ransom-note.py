#
# @lc app=leetcode id=383 lang=python
#
# [383] Ransom Note
#

# @lc code=start
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        freq = {}

        for char in magazine:
            freq[char] = freq.get(char, 0) + 1

        for char in ransomNote:
            if freq[char] == 0:
                return False
            freq[char] -= 1

        return True

# @lc code=end
