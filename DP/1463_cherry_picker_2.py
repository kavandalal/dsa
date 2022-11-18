# LINKS https://www.youtube.com/watch?v=QGfn7JeXK54&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=14&ab_channel=takeUforward

class Solution:

    #   recursion
    #   TC - (3^n * 3^n)
    #   SC - (n)(stack space)
    def solve1(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def recur(i, j1, j2):
            if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
                return -float('inf')

            if i == n-1:
                return grid[i][j1] if j1 == j2 else grid[i][j1] + grid[i][j2]

            maxi = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    val = 0
                    if j1 == j2:
                        val = grid[i][j1]
                    else:
                        val = grid[i][j1] + grid[i][j2]
                    val += recur(i+1, j1+x, j2+y)
                    maxi = max(maxi, val)
            return maxi

        return recur(0, 0, m-1)

#    DP
#    TC - O(n*m*m) X 9
#    SC - O(n*m*m) * O(n)(stack space)
    def solve2(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[[-1 for _ in range(m)] for _ in range(m)] for _ in range(n)]

        def recur(i, j1, j2):
            if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
                return -float('inf')

            if i == n-1:
                return grid[i][j1] if j1 == j2 else grid[i][j1] + grid[i][j2]
            if dp[i][j1][j2] != -1:
                return dp[i][j1][j2]

            maxi = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    val = 0
                    if j1 == j2:
                        val = grid[i][j1]
                    else:
                        val = grid[i][j1] + grid[i][j2]
                    val += recur(i+1, j1+x, j2+y)
                    maxi = max(maxi, val)

            dp[i][j1][j2] = maxi
            return maxi

        return recur(0, 0, m-1)

#    Tabulation
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[[-1 for _ in range(m)] for _ in range(m)] for _ in range(n)]

#         base case
        for j1 in range(0, m):
            for j2 in range(0, m):
                if j1 == j2:
                    dp[n-1][j1][j2] = grid[n-1][j1]
                else:
                    dp[n-1][j1][j2] = grid[n-1][j1] + grid[n-1][j2]

#           execute code
        for i in range(n-2, -1, -1):
            for j1 in range(0, m):
                for j2 in range(0, m):

                    maxi = -float('inf')
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            val = 0
                            if j1 == j2:
                                val = grid[i][j1]
                            else:
                                val = grid[i][j1] + grid[i][j2]
                            if j1+x >= 0 and j1+x < m and j2+y >= 0 and j2+y < m:
                                val += dp[i+1][j1+x][j2+y]
                            else:
                                val += -float('inf')
                            maxi = max(maxi, val)
                    dp[i][j1][j2] = maxi

        return dp[0][0][m-1]
