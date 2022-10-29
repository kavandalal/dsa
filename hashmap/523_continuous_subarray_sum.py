# LINKS https://www.youtube.com/watch?v=OKcrLfR-8mE

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainder = {0: -1}  # HASH MAP of remainder -> end index
        total = 0

        for i, v in enumerate(nums):
            total += v
            r = total % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True

        return False
