#
# @lc app=leetcode id=2798 lang=python
#
# [2798] Number of Employees Who Met the Target
#

# @lc code=start
class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        total = 0
        for hour in hours:
            if hour >= target:
                total += 1

        return total

    # O(n) T, O(1) S


# @lc code=end
