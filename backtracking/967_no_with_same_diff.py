# 967 LEETCODE - Numbers With Same Consecutive Differences


class Solution:
    def solve(self, n, k):
        res = []
        path = []

        def backtracking(index):
            if index == n:
                res.append(path[:])
                return
            for i in range(0, 10):
                if len(path) == 0 and i != 0:
                    path.append(i)
                    backtracking(index+1)
                    path.pop()
                else:
                    # abs(path[-1] + i) == k
                    if len(path) != 0 and abs(path[-1] - i) == k:
                        path.append(i)
                        backtracking(index + 1)
                        path.pop()
        backtracking(0)
        res = [int(''.join(map(str, i))) for i in res]
        return res


if __name__ == '__main__':
    x = Solution()
    n = 3
    k = 7
    print(x.solve(n, k))
