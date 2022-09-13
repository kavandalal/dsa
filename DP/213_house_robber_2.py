# 213 - LEETCODE - House Robber 2
# https://leetcode.com/problems/house-robber-ii/
# this is the problem same as the house robber 1, but in this our answer will not include both the first and the last element together in the final answer
# so what we can do is calculate the ans1( without first element) and ans2 (without last element)
# max of both of these answer will be our answer

#  edge case what if the array is of only size 1 - return that element as the answer


class Solution:

    def main(self, y):
        temp1 = y[1:]
        temp2 = y[: -1]
        if len(y) == 1:
            return y[0]
        return max(self.solve(temp1), self.solve(temp2))

    # dynamic problem with tabulation (space optimisation)
    # TC - O(n) , SC - O(1)
    def solve(self, y):
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
    y = [2, 3, 2]
    print(x.main(y))

# LINKS https://www.youtube.com/watch?v=3WaxQMELSkw
