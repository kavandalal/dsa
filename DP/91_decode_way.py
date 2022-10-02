# 91 LEETCODE Decode Way


class Solution:

    def solve(self, s: str) -> int:
        dp = {len(s): 1}

        for i in range(len(s) - 1, -1, -1):
            # base case
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            # functionality
            if (i + 1 < len(s) and (s[i] == '1' or (s[i] == "2" and s[i+1] in '0123456'))):
                dp[i] += dp[i + 2]
        return dp[0]

    def solve2(self, s: str) -> int:
        dp = {len(s): 1}

        def backtrack(i):
            # base case
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0

            # functionality
            result = backtrack(i+1)
            if (i + 1 < len(s) and (s[i] == '1' or (s[i] == "2" and s[i+1] in '0123456'))):
                result += backtrack(i+2)

            # store and return
            dp[i] = result
            return result

        return backtrack(0)


if __name__ == '__main__':
    x = [[10, 50, 5], [5, 100, 25]]
    s = Solution()
    # s.solve(x)
    s.solve2(x)
