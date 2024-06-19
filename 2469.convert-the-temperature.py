#
# @lc app=leetcode id=2469 lang=python
#
# [2469] Convert the Temperature
#

# @lc code=start
class Solution(object):
    def convertTemperature(self, celsius):
        ans = []
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.8 + 32.00

        ans.append(kelvin)
        ans.append(fahrenheit)

        return ans

    # O(1) T, O(1) S
# @lc code=end
