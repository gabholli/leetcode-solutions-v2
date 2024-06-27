#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        return max(freq, key=freq.get)

    # O(n) T O(n) S
# @lc code=end
