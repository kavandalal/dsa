# 55 - Jump Game - LEETCODE
# this problem can be solved by backtracking, dynamic prgramming, but the solution shown below is the best as TC - O(n), SC - O (1)

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        reachable = 0
        for i in range(n):
            if reachable < i:
                return False
            reachable = max(reachable, nums[i] + i)
        return True


if __name__ == '__main__':
    # nums = [2, 3, 1, 1, 4]  # True
    nums = [3, 2, 1, 0, 4]  # False
    x = Solution()
    print(x.canJump(nums))

# LINKS https://www.youtube.com/watch?v=muDPTDrpS28
