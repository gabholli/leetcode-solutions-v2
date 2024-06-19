#
# @lc app=leetcode id=1431 lang=python
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        highest_candies = 0
        result = [False] * len(candies)
        for i in range(len(candies)):
            highest_candies = candies[i] + extraCandies
            if highest_candies >= max(candies):
                result[i] = True

        return result

    # O(n) T, O(1) S

# @lc code=end
