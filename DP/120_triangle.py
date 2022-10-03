class Solution:
    # memoisation dp
    # TC - O(2^n)
    # SC - O(n*n)(dp varaiable) + O(n)(stack space)
    def solve1(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        dp = [[-1 for j in range(n)] for i in range(n)]

        def backtrack(i, j):
            if i == n-1:
                return triangle[n-1][j]
            if dp[i][j] != -1:
                return dp[i][j]
            down = triangle[i][j] + backtrack(i+1, j)
            diagonal = triangle[i][j] + backtrack(i+1, j+1)
            dp[i][j] = min(down, diagonal)
            return dp[i][j]
        return backtrack(0, 0)
    # tabulation dp
    # TC - O(n^n)
    # SC - O(n*n)(dp varaiable)

    def solve2(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        dp = [[-1 for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[n-1][i] = triangle[n-1][i]
        for i in range(n-2, -1, -1):
            for j in range(i, -1, -1):
                down = triangle[i][j] + dp[i+1][j]
                diagonal = triangle[i][j] + dp[i+1][j+1]
                dp[i][j] = min(down, diagonal)
        return dp[0][0]
    # Optimisation
    # TC - O(n^n)
    # SC - O(1)

    def solve3(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        nextRow = [0 for i in range(n)]
        curRow = [0 for x in range(n)]
        for i in range(n):
            nextRow[i] = triangle[n-1][i]
        for i in range(n-2, -1, -1):
            for j in range(i, -1, -1):
                down = triangle[i][j] + nextRow[j]
                diagonal = triangle[i][j] + nextRow[j+1]
                curRow[j] = min(down, diagonal)
            nextRow = curRow.copy()
        return nextRow[0]

# https://www.youtube.com/watch?v=SrP-PiLSYC0&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=12
