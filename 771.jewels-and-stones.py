#
# @lc app=leetcode id=771 lang=python
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        freq = {}
        counter = 0
        for stone in stones:
            freq[stone] = freq.get(stone, 0) + 1

        for jewel in jewels:
            if jewel in freq:
                counter += freq[jewel]

        return counter

    # O(m + n) T, O(m) S


# @lc code=end
