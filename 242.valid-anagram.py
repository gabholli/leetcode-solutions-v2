#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        freq = {}

        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

        for char in t:
            if char not in freq:
                freq[char] = -1
            else:
                freq[char] -= 1

        for value in freq.values():
            if value != 0:
                return False

        return True

    # O(m + n) T, O(1) S

# @lc code=end
