class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        prev = [0 for i in range(n)]
        for i in range(m):
            cur = [0 for i in range(n)]
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    cur[j] = 0
                elif i == 0 and j == 0:
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
