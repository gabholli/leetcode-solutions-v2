#
# @lc app=leetcode id=2011 lang=python
#
# [2011] Final Value of Variable After Performing Operations
#

# @lc code=start
class Solution(object):
    def finalValueAfterOperations(self, operations):
        x = 0
        for operation in operations:
            if operation == "++X" or operation == "X++":
                x += 1
            elif operation == "--X" or operation == "X--":
                x -= 1

        return x

    # O(n) T, O(1) S

# @lc code=end
