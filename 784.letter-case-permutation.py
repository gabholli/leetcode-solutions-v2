#
# @lc app=leetcode id=784 lang=python
#
# [784] Letter Case Permutation
#

# @lc code=start
class Solution(object):
    def letterCasePermutation(self, s):
        permutations = []
        permutations.append(s)

        for i in range(len(s)):
            char = s[i]
            if not char.isdigit():
                for j in range(len(permutations)):
                    chs = list(permutations[j])
                    chs[i] = chs[i].swapcase()
                    permutations.append(''.join(chs))
        return permutations

    # O(n * 2^n) T, O(n * 2^n) S

# @lc code=end
