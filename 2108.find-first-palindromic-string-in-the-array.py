#
# @lc app=leetcode id=2108 lang=python
#
# [2108] Find First Palindromic String in the Array
#

# @lc code=start
class Solution(object):
    def firstPalindrome(self, words):
        for word in words:
            if self.is_palindrome(word):
                return word

        return ''

    def is_palindrome(self, word):
        left, right = 0, len(word) - 1
        while left < right:
            if word[left] != word[right]:
                return False

            left += 1
            right -= 1

        return True

    # O(m + n) T, O(1) S
# @lc code=end
