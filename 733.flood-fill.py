#
# @lc app=leetcode id=733 lang=python
#
# [733] Flood Fill
#

# @lc code=start
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        if image[sr][sc] != color:
            self.helper(image, sr, sc, image[sr][sc], color)
        return image

    def helper(self, image, x, y, old_color, color):
        if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]):
            return

        if image[x][y] != old_color:
            return

        image[x][y] = color

        self.helper(image, x + 1, y, old_color, color)
        self.helper(image, x - 1, y, old_color, color)
        self.helper(image, x, y + 1, old_color, color)
        self.helper(image, x, y - 1, old_color, color)

    # O(mn) T, O(mn) S

# @lc code=end
