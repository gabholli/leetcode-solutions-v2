#
# @lc app=leetcode id=844 lang=python
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution(object):
    def backspaceCompare(self, s, t):
        index1, index2 = len(s) - 1, len(t) - 1

        while index1 >= 0 or index2 >= 0:
            i1 = self.helper(s, index1)
            i2 = self.helper(t, index2)

            if i1 < 0 and i2 < 0:
                return True

            if i1 < 0 or i2 < 0:
                return False

            if s[i1] != t[i2]:
                return False

            index1 = i1 - 1
            index2 = i2 - 1

        return True

    def helper(self, string, index):
        backspaces = 0

        while index >= 0:
            if string[index] == '#':
                backspaces += 1
            elif backspaces > 0:
                backspaces -= 1
            else:
                break

            index -= 1

        return index

    # O(m + n) T, O(1) S

# @lc code=end
