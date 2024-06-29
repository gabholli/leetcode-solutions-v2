#
# @lc app=leetcode id=2455 lang=python
#
# [2455] Average Value of Even Numbers That Are Divisible by Three
#

# @lc code=start
class Solution(object):
    def averageValue(self, nums):
        temp = []
        for num in nums:
            if num % 2 == 0 and num % 3 == 0:
                temp.append(num)
        avg = sum(temp) // len(temp)

        return avg

    # O(n) T, O(n) S

# @lc code=end
