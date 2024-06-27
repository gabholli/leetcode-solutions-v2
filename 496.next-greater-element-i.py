#
# @lc app=leetcode id=496 lang=python
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        freq = {}

        for num in nums2:
            while stack and stack[-1] < num:
                freq[stack.pop()] = num
            stack.append(num)

        return [freq.get(num, -1) for num in nums1]

    # O(n) T O(n) S

# @lc code=end
