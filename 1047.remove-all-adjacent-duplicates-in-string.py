#
# @lc app=leetcode id=1047 lang=python
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, s):
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)

    # O(n) T, (n) S

# @lc code=end
