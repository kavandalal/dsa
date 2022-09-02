# 37. Sudoku Solver

class Solution:

    def solveSudoku(self, board: list[list[str]]) -> None:
        self.solve(board)

    def solve(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for k in range(1, 10):
                        if self.is_valid(board, i, j, str(k)):
                            board[i][j] = str(k)
                            if self.solve(board) == True:
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    def is_valid(self, board, row, col, c):
        for i in range(9):
            if board[i][col] == c:
                # condition to check no duplicate in column
                return False
            if board[row][i] == c:
                # condition to check no duplicate in row
                return False
            if board[3 * (row // 3) + (i // 3)][3 * (col//3) + (i % 3)] == c:
                # condition to check no duplicate element in the sub matrix
                return False
        return True


if __name__ == '__main__':
    x = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                      ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    y = Solution()
    y.solve(x)
    print(x)
