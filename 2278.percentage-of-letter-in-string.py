#
# @lc app=leetcode id=2278 lang=python
#
# [2278] Percentage of Letter in String
#

# @lc code=start
class Solution(object):
    def percentageLetter(self, s, letter):
        letter_freq = {}
        for char in s:
            letter_freq[char] = letter_freq.get(char, 0) + 1

        if letter in letter_freq:
            print(letter_freq[letter] / len(s))

# @lc code=end
