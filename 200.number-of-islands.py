#
# @lc app=leetcode id=200 lang=python
#
# [200] Number of Islands
#

# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        number_of_islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    number_of_islands += 1
                    self.helper(grid, i, j)

        return number_of_islands

    def helper(self, grid, x, y):
        neighbors = []
        neighbors.append((x, y))
        while neighbors:
            row, col = neighbors.pop(0)

            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                continue

            if grid[row][col] == '0':
                continue

            grid[row][col] = '0'

            neighbors.extend([(row + 1, col)])
            neighbors.extend([(row - 1, col)])
            neighbors.extend([(row, col + 1)])
            neighbors.extend([(row, col - 1)])

    # O(mn) T, O(min(m ,n)) S

# @lc code=end
