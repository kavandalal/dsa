# 51 LEETCODE - N QUEEN

class Solution:

    def solve(self, n) -> list[list[str]]:
        col = set()  # the names of columns that are already taken in the permuations
        posDiag = set()  # r + c # diagonal elements that are present in the form of backward slash will alwasy have sum of their diagonals == row + column
        negDiag = set()  # r - c # diagonal elements that are present in the form of forward slash will always have substraction of their diagonal == row - column

        # making n * n board to keep track of elements
        board = [['.'] * n for _ in range(n)]
        res = []  # the result variable

        def backtracking(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return
            else:
                for c in range(n):
                    # if the column/diagonal/row is already taken
                    if c in col or (r+c) in posDiag or (r - c) in negDiag:
                        continue
                    col.add(c)
                    posDiag.add(r + c)
                    negDiag.add(r - c)
                    board[r][c] = 'Q'

                    backtracking(r + 1)

                    col.remove(c)
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)
                    board[r][c] = '.'

        backtracking(0)
        return res


if __name__ == '__main__':
    X = Solution()
    print(X.solve(4))

# LINKS https://www.youtube.com/watch?v=Ph95IHmRp5M
