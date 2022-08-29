# 90 - LEETCODE - Subset 2

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        # STRIVER
        # https://www.youtube.com/watch?v=RIn3gOkbhQE
        # takes more time and harder to understand
        def backtrack1(pos, ansArr):
            res.append(ansArr.copy())
            for i in range(pos, len(nums)):
                if i != pos and nums[i - 1] == nums[i]:
                    continue
                ansArr.append(nums[i])
                backtrack1(i + 1, ansArr)
                ansArr.pop()
                prev = nums[i]

        # NEETCODE
        # https://www.youtube.com/watch?v=Vn2v6ajA7U0
        # better solution that 1st
        def backtrack2(pos, ansArr):
            if len(nums) == pos:
                res.append(ansArr.copy())
                return

            # include all the path that include nums[pos]
            ansArr.append(nums[pos])
            backtrack2(pos + 1, ansArr)
            ansArr.pop()

            # dont include all the path that include nums[pos]
            while pos + 1 < len(nums) and nums[pos] == nums[pos + 1]:
                pos += 1
            backtrack2(pos + 1, ansArr)

        # backtrack1(0, [])
        backtrack2(0, [])
        return res


if __name__ == '__main__':
    x = Solution()
    a = [1, 2, 2]
    print(x.subsetsWithDup(a))

# NEETCODE
# https://www.youtube.com/watch?v=Vn2v6ajA7U0
