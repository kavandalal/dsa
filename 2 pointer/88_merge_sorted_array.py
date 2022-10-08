class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = m - 1
        right = n - 1
        ansi = m + n - 1
        while left >= 0 and right >= 0:
            if nums1[left] > nums2[right]:
                nums1[ansi] = nums1[left]
                ansi -= 1
                left -= 1
            else:
                nums1[ansi] = nums2[right]
                ansi -= 1
                right -= 1
        while right >= 0:
            nums1[ansi] = nums2[right]
            ansi -= 1
            right -= 1
