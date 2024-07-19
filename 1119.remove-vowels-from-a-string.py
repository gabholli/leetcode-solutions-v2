#
# @lc app=leetcode id=1119 lang=python
#
# [1119] Remove Vowels from a String
#

# @lc code=start
class Solution(object):
    def removeVowels(self, s):
        vowels = 'aeiouAEIOU'
        ans = []
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and vowels.find(s[l]) == -1:
                l += 1
            while l < r and vowels.find(s[r]) == -1:
                r -= 1

            ans.remove(s[l])
            ans.remove(s[r])

            l += 1
            r -= 1

        return ans

# @lc code=end
