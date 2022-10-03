class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[-1 for i in range(target+1)] for j in range(n + 1)]

        def backtrack(n, k, target):
            if n < 0 or target < 0:
                return 0
            if n == 0 and target == 0:
                return 1
            if dp[n][target] != -1:
                return dp[n][target]
            totalWays = 0
            for i in range(1, k+1):
                if i <= target:
                    totalWays = (totalWays + backtrack(n-1,
                                 k, target-i)) % 1000000007
            dp[n][target] = totalWays
            return totalWays
        return backtrack(n, k, target)

# LINKS https://www.youtube.com/watch?v=JfRxkDOP7-4
