#
# @lc app=leetcode id=2396 lang=python
#
# [2396] Strictly Palindromic Number
#

# @lc code=start
class Solution(object):
    def isStrictlyPalindromic(self, n):
        string_num = self.decimal_to_binary(n)
        print(string_num)
        l, r = 0, len(string_num) - 1

        while l < r:
            if string_num[l] != string_num[r]:
                return False

            l += 1
            r -= 1

        return True

    def decimal_to_binary(self, n):
        stack = []

        while n > 0:
            stack.append(n % 2)
            n //= 2

        return ''.join([str(i) for i in reversed(stack)])


# @lc code=end
