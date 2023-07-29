# LEETCODE 416
# https://www.youtube.com/watch?v=7win3dcgo3k&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=16

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        def getEqualBool(target) -> int: 
            prev = [False for _ in range(target+1)]
            prev[0] = True
            
            for j in range(n): 
                cur = [False for i in range(target+1)]
                for k in range(target+1): 
                    notTake = prev[k]
                    take = False 
                    if nums[j] <= k: 
                        take =  prev[k - nums[j]]
                    
                    cur[k] = take or notTake
                prev = cur
            
            return prev[target]

        n = len(nums)
        sumx =  sum(nums)
        if sumx % 2 != 0 : 
            return False
        

        return getEqualBool(sumx//2)