#
# @lc app=leetcode id=921 lang=python
#
# [921] Minimum Add to Make Parentheses Valid
#

# @lc code=start
class Solution(object):
    def minAddToMakeValid(self, s):
        balance, counter = 0, 0

        for c in s:
            balance += 1 if c == "(" else -1
            if balance == -1:
                balance += 1
                counter += 1

        return balance + counter

    # O(n) T, O(1) S

# @lc code=end
