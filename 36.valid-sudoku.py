#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for num in range(1, 10):
                        if self.helper(board, row, col, str(num)):
                            board[row][col] = str(num)
                            if self.isValidSudoku(board):
                                return True
                            else:
                                board[row][col] = '.'
                    return False
        return True

    def helper(self, board, row, col, num):
        for x in range(9):
            if board[row][x] == num:
                return False
            if board[x][col] == num:
                return False
            if board[(row // 3) * 3 + x // 3][(col // 3) * 3 + x % 3] == num:
                return False

        return True

    # O(1) T, O(1) S
# @lc code=end
