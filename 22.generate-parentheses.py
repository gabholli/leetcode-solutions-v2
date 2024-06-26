#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#

# @lc code=start

class ParenthesesString:

    def __init__(self, string, open_count, close_count):
        self.string = string
        self.open_count = open_count
        self.close_count = close_count


class Solution(object):
    def generateParenthesis(self, n):
        result = []
        queue = []
        queue.append(ParenthesesString("", 0, 0))

        while queue:
            ps = queue.pop(0)
            if ps.open_count == n and ps.close_count == n:
                result.append(ps.string)
            else:
                if ps.open_count < n:
                    queue.append(ParenthesesString(
                        ps.string + "(", ps.open_count + 1, ps.close_count))
                if ps.open_count > ps.close_count:
                    queue.append(ParenthesesString(ps.string + ")",
                                 ps.open_count, ps.close_count + 1))

        return result

    # O(n * 2^n) T ,O(n * 2^n) S
# @lc code=end
