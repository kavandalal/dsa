# 198 - LEETCODE - House Robber
# https://leetcode.com/problems/house-robber/

class Solution:

    # plain recursion time limit will exceed normally but will work perfectly for less numbers
    # TC - O(2^n) , SC - O(n)(stack space)
    def solve(self, y):
        n = len(y)

        def backtrack(idx):
            if idx == 0:
                return y[idx]
            if idx < 0:
                return 0
            pick = y[idx] + backtrack(idx - 2)
            not_pick = 0 + backtrack(idx - 1)
            return max(pick, not_pick)
        return backtrack(n - 1)

    # recursion with dp array (memoization)
    # TC - O(2^n) (less than that), SC - O(n)(stack space) + O(n)(dp array)
    # will not show time limit exceed
    def solve2(self, y):
        n = len(y)
        dp = [-1] * n

        def backtrack(idx):
            if dp[idx] != -1:
                return dp[idx]
            if idx == 0:
                return y[idx]
            if idx < 0:
                return 0
            pick = y[idx] + backtrack(idx - 2)
            not_pick = 0 + backtrack(idx - 1)
            dp[idx] = max(pick, not_pick)
            return dp[idx]
        return backtrack(n - 1)

    # dynamic problem with tabulation
    # TC - O(n) , SC - O(n)(dp array)
    def solve3(self, y):
        n = len(y)
        dp = [-1] * n
        dp[0] = y[0]
        for i in range(1, n):
            pick = y[i]
            if i > 1:
                pick += dp[i-2]
            not_pick = 0 + dp[i - 1]
            dp[i] = max(pick, not_pick)
        return dp[-1]

    # dynamic problem with tabulation (space optimisation)
    # TC - O(n) , SC - O(1)
    def solve4(self, y):
        n = len(y)
        prev = y[0]  # dp[0]
        prev2 = 0  # negative index
        for i in range(1, n):
            pick = y[i]
            if i > 1:
                pick += prev2
            not_pick = 0 + prev
            curi = max(pick, not_pick)
            prev2 = prev
            prev = curi
        return prev


if __name__ == '__main__':
    x = Solution()
    y = [1, 2, 3, 1]
    print(x.solve(y))
    print(x.solve2(y))
    print(x.solve3(y))
    print(x.solve4(y))


# LINKS https://www.youtube.com/watch?v=GrMBfJNk_NY&t=118s
