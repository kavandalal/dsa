class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
            print(xor)

        return xor

# LINKS https://leetcode.com/problems/single-number/discuss/1771771/Think-it-through-oror-Time%3A-O(n)-Space%3A-O(1)-oror-Python-Explained
