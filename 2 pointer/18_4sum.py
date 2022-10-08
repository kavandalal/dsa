class Solution:
  # TC - O(n^3 x nlogn(for sorting))
  # SC - O(n)
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        x = len(nums)
        if x < 4:
            return []
        output = []
        nums.sort()

        for i in range(x-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, x-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j+1
                right = x-1

                while left < right:
                    sumHere = nums[i] + nums[j] + nums[left] + nums[right]
                    if sumHere == target:
                        output.append(
                            [nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                    elif sumHere < target:
                        left += 1
                    else:
                        right -= 1
        return output
