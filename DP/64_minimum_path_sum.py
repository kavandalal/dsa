class Solution:
    # memoization with recurrsion
    # TC - O(m*n)
    # SC - O((m-1) + (n-1))(path length/stack) + O(m*n)(dp array)
    def solve1(self, grid: list[list[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        dp = [[-1 for j in range(c)] for i in range(r)]

        def backtrack(i, j):
            if i < 0 or j < 0:
                return float('inf')
            elif i == 0 and j == 0:
                return grid[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            up = grid[i][j] + backtrack(i-1, j)
            left = grid[i][j] + backtrack(i, j-1)
            dp[i][j] = min(up,  left)
            return dp[i][j]
        return backtrack(r-1, c-1)
    # Tabulation
    # TC - O(m*n)
    # SC - O(m*n)(dp array)

    def solve2(self, grid: list[list[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        dp = [[-1 for j in range(c)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                else:
                    up = grid[i][j]
                    if i > 0:
                        up += dp[i-1][j]
                    else:
                        up += float('inf')
                    left = grid[i][j]
                    if j > 0:
                        left += dp[i][j-1]
                    else:
                        left += float('inf')
                    dp[i][j] = min(up, left)
        return dp[r-1][c-1]
    # Optimisation
    # TC - O(m*n)
    # SC - O(1)

    def solve3(self, grid: list[list[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        prevRow = [0 for x in range(c)]
        for i in range(r):
            curRow = [0 for x in range(c)]
            for j in range(c):
                if i == 0 and j == 0:
                    curRow[j] = grid[i][j]
                else:
                    up = grid[i][j]
                    if i > 0:
                        up += prevRow[j]
                    else:
                        up += float('inf')
                    left = grid[i][j]
                    if j > 0:
                        left += curRow[j-1]
                    else:
                        left += float('inf')
                    curRow[j] = min(up, left)
            prevRow = curRow
        return prevRow[c-1]


# https://www.youtube.com/watch?v=_rgTlyky1uQ&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=11
