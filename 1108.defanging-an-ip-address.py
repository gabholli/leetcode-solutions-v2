#
# @lc app=leetcode id=1108 lang=python
#
# [1108] Defanging an IP Address
#

# @lc code=start
class Solution(object):
    def defangIPaddr(self, address):
        return address.replace('.', "[.]")

    # O(n) T, O(1) S

# @lc code=end
