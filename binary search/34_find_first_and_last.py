
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lefti = -1
        righti = -1

        l = 0
        r = len(nums)-1
        # for leftmost
        while l <= r:
            mid = l + ((r - l)//2)
            if nums[mid] == target:
                r = mid - 1
                lefti = mid
            elif nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid - 1

        l = 0
        r = len(nums)-1
        # for rightmost
        while l <= r:
            mid = l + ((r - l)//2)
            if nums[mid] == target:
                l = mid + 1
                righti = mid
            elif nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid - 1
        return [lefti, righti]


# LINKS https://www.youtube.com/watch?v=zD2Jg3alZV8&list=PLDzeHZWIZsTryvtXdMr6rPh4IDexB5NIA&index=13
