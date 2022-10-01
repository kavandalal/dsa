# Ninja's training
# https: // www.codingninjas.com/codestudio/problems/ninja-s-training_3621003


class Solution:

    # Recuression
    # TC - O(3^n) , SC - O(n)(stack space)
    def solve(self, tasks):
        n = len(tasks)

        def backtrack(day,  lastUsed):
            if day == 0:
                maxi = 0
                for i in range(3):
                    if i != lastUsed:
                        maxi = max(maxi, tasks[0][i])
                return maxi

            maxi2 = 0
            for i in range(3):
                if i != lastUsed:
                    point = tasks[day][i] + backtrack(day - 1, i)
                    maxi2 = max(maxi2, point)
            return maxi2

        print(backtrack(n-1, 3))

    # Memoisation
    # TC - O( <3^n) , SC - O(n^2)(dp array)
    def solve2(self, tasks):
        n = len(tasks)
        dp = [[-1 for i in range(4)] for j in range(n)]

        def backtrack(day, lastUsed):
            if day == 0:
                maxi = 0
                for i in range(3):
                    if i != lastUsed:
                        maxi = max(maxi, tasks[0][i])
                return maxi

            if dp[day][lastUsed] != -1 and lastUsed != 3:
                return dp[day][lastUsed]

            maxi2 = 0
            for i in range(3):
                if i != lastUsed:
                    point = tasks[day][i] + backtrack(day-1,  i)
                    maxi2 = max(maxi2, point)
            dp[day][lastUsed] = maxi2
            return dp[day][lastUsed]

        print(backtrack(n - 1, 3))


if __name__ == '__main__':
    x = [[10, 50, 5], [5, 100, 25]]
    s = Solution()
    # s.solve(x)
    s.solve2(x)
