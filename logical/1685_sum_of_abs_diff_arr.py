# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/description/?envType=daily-question&envId=2023-11-25


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n=len(nums)
        leftSum = 0 # sum of elements till now, if i == 0, leftSum = 0
        total = sum(nums) # total sum of all right elements
        ans = [0] * n 
        for i, x in enumerate(nums): 
            ans[i] = ((x*i) - leftSum) + (total - x * (n-i))
            # ((x*i) - leftSum) 
            # as the elements on the left are smaller than x, we write (x*i) - leftSum 
            # ( total - x * (n-i))
            # as the elements on the right are bigger than x, we write (total - x * (n-i)), (n - i) because we dont want to count the left elements of x
            leftSum += x
            total -= x
        
        return ans