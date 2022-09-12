# 403 - LEETCODE - FROG JUMP
# https://leetcode.com/problems/frog-jump/

class Solution:

    def solve(self, x, n):
        mainDict = dict()
        for i in x:
            mainDict[i] = set()
        mainDict[0].add(1)
        for i in range(0, n):
            curStone = x[i]
            for jump in mainDict[curStone]:
                position = curStone + jump
                if position == x[-1]:
                    return True
                if position in mainDict:
                    if jump - 1 > 0:
                        mainDict[position] .add(jump - 1)
                    mainDict[position].add(jump)
                    mainDict[position].add(jump + 1)
        return False


if __name__ == '__main__':
    x = Solution()
    y = [0, 1, 3, 5, 6, 8, 12, 17]  # TRUE
    # y = [0, 1, 2, 3, 4, 8, 9, 11] # FALSE
    print(x.solve(y, len(y)))

# LINKS https://www.youtube.com/watch?v=1V8gRXh1qbU
