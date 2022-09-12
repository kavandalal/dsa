class Solution:

    # TC - O(n) , SC - O(n) (dp variable)
    def solve(self, n):
        dp = [-1] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i - 2]
        print(dp[n])

    # TC - O(n) , SC - O(1) (only 3 variables used)
    def solve2(self, n):
        # dp = [-1] * (n + 1)
        prev2 = 1
        prev = 1
        for i in range(2, n+1):
            curi = prev + prev2
            prev2 = prev
            prev = curi
        print(prev)


if __name__ == '__main__':
    x = Solution()
    n = 4
    x.solve(3)
    x.solve2(3)
