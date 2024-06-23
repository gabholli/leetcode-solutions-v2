#
# @lc app=leetcode id=3005 lang=python
#
# [3005] Count Elements With Maximum Frequency
#

# @lc code=start
class Solution(object):
    def maxFrequencyElements(self, nums):
        freq = {}
        answer = 0
        max_value = 0
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for key, value in freq.items():
            max_value = max(max_value, value)
            if value == max_value:
                answer += value
        return answer

# @lc code=end
