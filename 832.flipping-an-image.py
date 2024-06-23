#
# @lc app=leetcode id=832 lang=python
#
# [832] Flipping an Image
#

# @lc code=start
class Solution(object):
    def flipAndInvertImage(self, image):
        col = len(image[0])
        for row in image:
            for i in range((col + 1) // 2):
                row[i], row[col - i - 1] = row[col - i - 1] ^ 1, row[i] ^ 1

        return image

    # O(n) T, O(1) S

# @lc code=end
