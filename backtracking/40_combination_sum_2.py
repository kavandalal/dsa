# 40 - LEETCODE - Combination Sum 2
# we need to find all the possible outcome which have sum equal to target given we have to sort each of the solution in ascending order and also should remove all the duplicates
# suppose list  = [1,2,3,7,1] and target = 8
# the solution could have [1,7] and [7,1]
# but we have to include only one of the above solutions
class Solution:
    def solve(self, arr: list[int], total: int) -> None:
        arr.sort()
        res = []

        def backtracking(pos,  ansArr, sumHere):
            if sumHere == 0:
                res.append(ansArr.copy())
            if sumHere <= 0:
                return

            prev = -1
            for i in range(pos,  len(arr)):
                if arr[i] == prev:
                    continue
                ansArr.append(arr[i])
                backtracking(i + 1, ansArr, sumHere - arr[i])
                ansArr.pop()
                prev = arr[i]
        backtracking(0, [], total)
        print(res)
        return


if __name__ == '__main__':
    x = Solution()
    a = [1, 3, 2, 6, 7, 1, 3]
    x.solve(a, 8)

# LINKS
# https://www.youtube.com/watch?v=rSA3t6BDDwg
# https://www.youtube.com/watch?v=G1fRTGRxXU8
