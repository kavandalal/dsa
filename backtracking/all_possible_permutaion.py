class Solution:
    def __init__(self):
        self.result = []

    def permute(self, nums_left) -> list[list[int]]:
        self.backtrack(nums_left, path=[])
        return self.result

    def backtrack(self,   nums_left, path):
        if not nums_left:
            self.result.append(path)
        for x in range(len(nums_left)):
            self.backtrack(nums_left[:x] +
                           nums_left[x+1:], path + [nums_left[x]])


if __name__ == '__main__':
    X = Solution()
    print(X.permute([1, 2, 3]))

# LINKS https://www.youtube.com/watch?v=DBLUa6ErLKw
