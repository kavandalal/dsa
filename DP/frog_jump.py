# FROG JUMP (N+1 OR N+2) (not from leetcode)
# https://www.codingninjas.com/codestudio/problem-details/frog-jump_3621012

import sys


class Solution:

    # recursion with dp array
    # TC - O(n) , SC - O(n)(dp array) + O (n) stack space
    def solve(self, x, n):
        dp = [-1] * (n)

        def backtrack(i):
            if i == 0:
                dp[0] = 0
                return 0
            if dp[i] != -1:
                return dp[i]
            left = backtrack(i-1) + abs(x[i] - x[i-1])
            right = sys.maxsize
            if i > 1:
                right = backtrack(i-2) + abs(x[i] - x[i - 2])
            dp[i] = min(left, right)
            print(dp)
            return dp[i]

        return backtrack(n-1)

    # dp problem, without dp array
    # TC - O(n) , SC - O(1)
    def solve2(self, x, n):
        prev = 0
        prev2 = 0
        for i in range(1, n):
            first_step = prev + abs(x[i] - x[i-1])
            second_step = sys.maxsize
            if i > 1:
                second_step = prev2 + abs(x[i] - x[i-2])
            curi = min(first_step, second_step)
            prev2 = prev
            prev = curi
        return prev


if __name__ == '__main__':
    x = Solution()
    y = [30, 10, 60, 10, 60, 50]
    n = len(y)
    print(x.solve(y, n))
    print(x.solve2(y, n))

# LINKS https://www.youtube.com/watch?v=EgG3jsGoPvQ&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=4
