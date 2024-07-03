#
# @lc app=leetcode id=744 lang=python
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        n = len(letters)

        start, end = 0, n - 1

        while start <= end:
            mid = start + (end - start) // 2

            if target > letters[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return letters[start % n]

# @lc code=end
