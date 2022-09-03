# Rat in a maze
# In this problem the rat is at current location (0,0) and want to go to (n-1,n-1) location. We have to find all the possible ways in which the rat can travel to (n-1,n-1).
# Done using recursion
# n = number of NxN block maze
# m == maze
# 0 in maze indicated there is a wall
# 1 indicated there is possible path


class Solution:
    def solve(self, n, k):
        res = []
        path = []
        visited = []
        directions = {'D': {'row': 1, 'col': 0},
                      'U': {'row': -1, 'col': 0},
                      'L': {'row': 0, 'col': -1},
                      'R': {'row': 0, 'col': 1},
                      }

        def backtracking(row, col):
            if row == n-1 and col == n-1:
                res.append(path[:])
                return
            if row < 0 or col < 0 or row >= n or col >= n:
                return
            if k[row][col] == 0:
                return
            for i in directions:
                if (row, col) not in visited:
                    path.append(i)
                    visited.append((row, col))
                    backtracking(
                        row + directions[i]['row'], col + directions[i]["col"])
                    visited.pop()
                    path.pop()

        backtracking(0, 0)
        res = [''.join(i) for i in res]
        return res


if __name__ == '__main__':
    x = Solution()
    n = 4
    m = [[1, 1, 1, 0],
         [0, 1, 1, 1],
         [0, 1, 0, 0],
         [0, 1, 1, 1]]
    print(x.solve(n, m))


# LINKS
# https://www.youtube.com/watch?v=bLGZhJlt4y0&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=18
