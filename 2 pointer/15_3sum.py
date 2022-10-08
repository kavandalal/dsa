class Solution:
  # TC - O(n^2 x nlogn(for sorting))
  # SC - O (n)
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        output = []
        # nums.sort()
        nums = sorted(nums)
        temp = sum(nums[:3])
        if temp > 0:
            return output
        temp = sum(nums[-3:])
        if temp < 0:
            return output
        x = len(nums)
        for i in range(x-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = x - 1
            while left < right:
                sumHere = nums[i] + nums[left] + nums[right]
                if sumHere == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif sumHere < 0:
                    left += 1
                else:
                    right -= 1

        return output
