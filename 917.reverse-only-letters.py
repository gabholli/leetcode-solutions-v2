#
# @lc app=leetcode id=917 lang=python
#
# [917] Reverse Only Letters
#

# @lc code=start
class Solution(object):
    def reverseOnlyLetters(self, s):
        array = list(s)

        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not array[left].isalpha():
                left += 1

            while left < right and not array[right].isalpha():
                right -= 1

            array[left], array[right] = array[right], array[left]

            left += 1
            right -= 1
        return ''.join(array)

    # O(n) T, O(n) S

# @lc code=end
