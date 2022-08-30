# LEETCODE 46 Permutation

class Solution:

    #  Approch 1 start, from Anish Malla https://www.youtube.com/watch?v=DBLUa6ErLKw
    def __init__(self):
        self.result = []

    def permute(self, nums_left) -> list[list[int]]:
        self.backtrack(nums_left, path=[])
        return self.result

    def backtrack1(self,   nums_left, path):
        if not nums_left:
            self.result.append(path)
        for x in range(len(nums_left)):
            self.backtrack(nums_left[:x] +
                           nums_left[x+1:], path + [nums_left[x]])

    # Approach 1 end

    # Approach 2 start, from Striver https://www.youtube.com/watch?v=YK78FU5Ffjw
    # better solution than above and easier to understand
    def solve(self, nums):
        res = []  # main ans variable
        freq = [False] * len(nums)
        # keeping track of which elements have been already taken

        def backtrack2(ansArr):
            if len(ansArr) == len(nums):
                res.append(ansArr[:])
                return
            for i in range(len(nums)):
                if not freq[i]:
                    freq[i] = True
                    ansArr.append(nums[i])
                    backtrack2(ansArr)
                    ansArr.pop()
                    freq[i] = False

        backtrack2([])
        print(res)
    # Approach 2 end


if __name__ == '__main__':
    X = Solution()
    a = ['X', 'Y', 'Z']
    # print(X.permute([1, 2, 3]))# Approach 1
    X.solve(a)  # Approach 2

# LINKS Striver https://www.youtube.com/watch?v=YK78FU5Ffjw
