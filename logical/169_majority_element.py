class Solution:
    # TC - O(nlogn) , SC - O(1)
    def majorityElement(self, nums: list[int]) -> int:
        l = len(nums)//2
        nums.sort()
        return nums[l]

    # TC - O(n) , SC - O(1)
    def majorityElement2(self, nums: list[int]) -> int:
        candidate, count = nums[0], 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate, count = num, 1
            else:
                count -= 1
        return candidate
