
class Solution:

    # memoisation
    # TC - O(3^n)(in simple recurssion) => O(n*n)
    # SC - O(n*n)(dp variable) + O(n)(stack space)
    def solve1(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        mini = float('inf')
        dp = [[-1 for j in range(n)] for i in range(n)]

        def backtrack(i, j):
            if j < 0 or j >= n:
                return float('inf')
            if i == 0:
                return matrix[0][j]
            if dp[i][j] != -1:
                return dp[i][j]

            upL = matrix[i][j] + backtrack(i-1, j-1)
            up = matrix[i][j] + backtrack(i-1, j)
            upR = matrix[i][j] + backtrack(i-1, j+1)

            dp[i][j] = min(up, upL, upR)
            return dp[i][j]

        for j in range(n):
            mini = min(mini, backtrack(n-1, j))
        return mini

    # tabulation
    # TC - O(n*n)
    # SC - O(n*n)(dp variable)
    def solve2(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        mini = float('inf')
        dp = [[-1 for j in range(n)] for i in range(n)]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        for i in range(1, n):
            for j in range(n):
                upL = float('inf')
                if j-1 >= 0:
                    upL = matrix[i][j] + dp[i-1][j-1]
                up = matrix[i][j] + dp[i-1][j]
                upR = float('inf')
                if j+1 < n:
                    upR = matrix[i][j] + dp[i-1][j+1]
                dp[i][j] = min(up, upL, upR)
        return min(dp[n-1])

    # tabulation
    # TC - O(n*n)
    # SC - O(1)
    def solve3(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        mini = float('inf')
        prevRow = [0 for i in range(n)]
        for j in range(n):
            prevRow[j] = matrix[0][j]

        for i in range(1, n):
            curRow = [0 for i in range(n)]
            for j in range(n):
                upL = float('inf')
                if j-1 >= 0:
                    upL = matrix[i][j] + prevRow[j-1]
                up = matrix[i][j] + prevRow[j]
                upR = float('inf')
                if j+1 < n:
                    upR = matrix[i][j] + prevRow[j+1]
                curRow[j] = min(up, upL, upR)
            prevRow = curRow
        return min(prevRow)

# LINKS https://www.youtube.com/watch?v=N_aJ5qQbYA0&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=13
