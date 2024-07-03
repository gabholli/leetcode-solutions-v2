#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        left, right = 0, len(x) - 1

        while left < right:
            if x[left] != x[right]:
                return False

            left += 1
            right -= 1

        return True

    # O(n) T, O(n) S

# @lc code=end
