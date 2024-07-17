#
# @lc app=leetcode id=345 lang=python
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution(object):
    def reverseVowels(self, s):
        vowels = 'aeiouAEIOU'
        array = list(s)

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and vowels.find(array[l]) == -1:
                l += 1

            while l < r and vowels.find(array[r]) == -1:
                r -= 1

            array[l], array[r] = array[r], array[l]

            l += 1
            r -= 1

        return ''.join(array)

# @lc code=end
