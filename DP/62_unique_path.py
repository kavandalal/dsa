# https://leetcode.com/problems/unique-paths/
# LEETCODE 62 - Unique paths

class Solution:
    # recurrsion
    # TC - O(2 ^ (m*n))
    # SC - O((m-1) + (n-1))(stack)
    def solve1(self, m: int, n: int) -> int:
        count = 0

        def backtrack(x, y):
            if x == 0 and y == 0:
                return 1
            if x < 0 or y < 0:
                return 0
            goLeft = backtrack(x-1, y)
            goUp = backtrack(x, y-1)
            return goLeft + goUp
        count = backtrack(m-1, n-1)
        return count

    # memoization
    # TC - O(m*n)
    # SC - O((m-1) + (n-1))(stack) + O(m*n)(dp array)
    def solve2(self, m: int, n: int) -> int:
        count = 0
        dp = [[-1 for i in range(n)] for j in range(m)]

        def backtrack(x, y):
            if dp[x][y] != -1:
                return dp[x][y]
            if x == 0 and y == 0:
                return 1
            if x < 0 or y < 0:
                return 0
            goLeft = backtrack(x-1, y)
            goUp = backtrack(x, y-1)
            dp[x][y] = goLeft + goUp
            return dp[x][y]
        count = backtrack(m-1, n-1)
        return count

    # tabulation
    # TC - O(m*n)
    # SC - O(m*n)
    def solve3(self, m: int, n: int) -> int:
        dp = [[-1 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = 1
                else:
                    up, left = 0, 0
                    if i != 0:
                        up = dp[i-1][j]
                    if j != 0:
                        left = dp[i][j-1]
                    dp[i][j] = up + left
        return dp[m-1][n-1]

    # optimization tabulation
    # TC - O(m*n)
    # SC - O(1)
    def solve4(self, m: int, n: int) -> int:
        prev = [0 for i in range(n)]
        for i in range(m):
            cur = [0 for i in range(n)]
            for j in range(n):
                if i == 0 and j == 0:
                    cur[j] = 1
                else:
                    up, left = 0, 0
                    if i != 0:
                        up = prev[j]
                    if j != 0:
                        left = cur[j-1]
                    cur[j] = up + left
            prev = cur
        return prev[n-1]


if __name__ == '__main__':
    x = Solution()
    m = 3
    n = 7
    print(x.solve1(m, n))
    print(x.solve2(m, n))
    print(x.solve3(m, n))
    print(x.solve4(m, n))


# LINKS https://www.youtube.com/watch?v=sdE0A2Oxofw&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=9
