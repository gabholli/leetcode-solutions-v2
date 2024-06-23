#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        subsets = []
        subsets.append([])

        for i in range(len(nums)):
            for j in range(len(subsets)):
                set1 = list(subsets[j])
                set1.append(nums[i])
                subsets.append(set1)

        return subsets

    # O(n * 2^n) T, O(n * 2^n) S

# @lc code=end
