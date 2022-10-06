class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = l + ((r-l)//2)
            if arr[mid] > arr[mid+1] and arr[mid-1] < arr[mid]:
                return mid
            if arr[mid] < arr[mid+1]:
                l = mid + 1
            else:
                if arr[mid-1] < arr[mid]:
                    r = mid
                else:
                    r = mid - 1

# LINKS https://www.youtube.com/watch?v=zD2Jg3alZV8&list=PLDzeHZWIZsTryvtXdMr6rPh4IDexB5NIA&index=13
