#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        result = []
        nums.sort()
        permutations = []
        permutations.append([])

        for num in nums:
            for _ in range(len(permutations)):
                old_permutation = permutations.pop(0)
                for j in range(len(old_permutation) + 1):
                    new_permutation = list(old_permutation)
                    new_permutation.insert(j, num)
                    if len(new_permutation) == len(nums):
                        result.append(new_permutation)
                    else:
                        permutations.append(new_permutation)

        return result

    # O(n * n!) T, O(n * n!) S

# @lc code=end
