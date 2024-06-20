#
# @lc app=leetcode id=1281 lang=python
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#

# @lc code=start
class Solution(object):
    def subtractProductAndSum(self, n):
        running_sum = 0
        running_product = 0
        for digit in str(n):
            running_sum += int(digit)
            running_product *= int(digit)

        print(running_product)
        print(running_sum)

        return running_product - running_sum


# @lc code=end
