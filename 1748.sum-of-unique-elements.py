#
# @lc app=leetcode id=1748 lang=python
#
# [1748] Sum of Unique Elements
#

# @lc code=start
class Solution(object):
    def sumOfUnique(self, nums):
        unique_nums = {}
        answer = 0
        for num in nums:
            unique_nums[num] = unique_nums.get(num, 0) + 1

        for key, value in unique_nums.items():
            if value == 1:
                answer += key

        return answer

    # O(n) T, O(n) S

# @lc code=end
