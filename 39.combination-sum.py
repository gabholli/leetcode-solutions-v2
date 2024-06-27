#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        return self.helper(candidates, 0, target, [], [])

    def helper(self, candidates, start, target, comb, res):
        if target == 0:
            res.append(list(comb))
            return

        for i in range(start, len(candidates)):
            if target < candidates[i]:
                continue

            comb.append(candidates[i])
            self.helper(candidates, i, target - candidates[i], comb, res)
            comb.pop()

        return res

    # O(n^t/m+1) T, O(t/m) S

# @lc code=end
