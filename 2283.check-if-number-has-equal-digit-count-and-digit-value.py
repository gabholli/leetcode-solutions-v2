#
# @lc app=leetcode id=2283 lang=python
#
# [2283] Check if Number Has Equal Digit Count and Digit Value
#

# @lc code=start
class Solution(object):
    def digitCount(self, num):
        freq = {}
        for digit in num:
            freq[digit] = freq.get(digit, 0) + 1

        for i, num in enumerate(num):
            print(freq[num])

    # O(n) T, O(n) S
# @lc code=end
