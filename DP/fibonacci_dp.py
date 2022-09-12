# Fibonacci using Dynamic Programming

class Solution:
    # TC - O(n) , SC - O(n) (stack) + O(n) (dp array)
    def solve(self, n):
        dp = [-1] * (n+1)

        def fibo(n):
            if n <= 1:
                return n
            if dp[n] != -1:
                return dp[n]
            dp[n] = fibo(n-1) + fibo(n - 2)
            return dp[n]
        print(fibo(n))

    # TC - O(n) , SC - O(n) (dp array)
    def solve2(self, n):
        dp = [-1] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        print(dp[n])

    # TC - O(n) , SC - O(1) (only 3 variables used)
    def solve3(self, n):
        prev2 = 0
        prev = 1
        for i in range(2, n+1):
            curi = prev + prev2
            prev2 = prev
            prev = curi
        print(prev)


if __name__ == '__main__':
    s = Solution()
    n = 7
    s.solve(n)
    s.solve2(n)
    s.solve3(n)

# LINKS - https://www.youtube.com/watch?v=tyB0ztf0DNY&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=2
