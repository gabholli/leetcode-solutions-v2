#
# @lc app=leetcode id=442 lang=python
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
class Solution(object):
    def findDuplicates(self, nums):
        i = 0
        n = len(nums)

        while i < n:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1


# @lc code=end
