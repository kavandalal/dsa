class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one, two = -1, -1, -1
        for i in range(len(nums)):
            if nums[i] == 0:
                two += 1
                nums[two] = 2
                one += 1
                nums[one] = 1
                zero += 1
                nums[zero] = 0
            elif nums[i] == 1:
                two += 1
                nums[two] = 2
                one += 1
                nums[one] = 1
            elif nums[i] == 2:
                two += 1
                nums[two] = 2
        return
