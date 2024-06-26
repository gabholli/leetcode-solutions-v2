#
# @lc app=leetcode id=463 lang=python
#
# [463] Island Perimeter
#

# @lc code=start
class Solution(object):
    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for x in range(cols)] for y in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    return self.helper(grid, visited, i, j)

        return 0

    def helper(self, grid, visited, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return 1

        if grid[x][y] == 0:
            return 1

        if visited[x][y]:
            return 0

        visited[x][y] = True

        perimeter = 0

        perimeter += self.helper(grid, visited, x + 1, y)
        perimeter += self.helper(grid, visited, x - 1, y)
        perimeter += self.helper(grid, visited, x, y + 1)
        perimeter += self.helper(grid, visited, x, y - 1)
        return perimeter

    # O(mn) T, O(mn) S

# @lc code=end
