# LEETCODE 494
# solution ref of getCount() - https://www.youtube.com/watch?v=fWX9xDmIzRI&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=16
# solution ref - https://leetcode.com/problems/target-sum/solutions/1470377/c-4ms-beats-98-similar-to-count-of-subset-with-given-sum-dp-explanation/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def getCount(ind , target) -> int: 
            prev = [0 for i in range(target+1)]
            if nums[0] == 0 : 
                prev[0] = 2  # as there are 0 in the nums too, then taking them or not taking them will be equal
            else : 
                prev[0] = 1 

            if nums[0] != 0 and nums[0] <= target:
                prev[nums[0]] = 1 
            
            for j in range(1,n): 
                cur = [0 for i in range(target+1)]
                for k in range(target+1): 
                    notTake = prev[k]
                    take = 0 
                    if nums[j] <= k: 
                        take =  prev[k - nums[j]]
                    
                    cur[k] = take + notTake
                prev = cur
            
            return prev[target]


        n = len(nums)
        summation = sum(nums)
        if ( abs(target) > summation) or ((summation + target) % 2 != 0 ): 
            return 0

        s1 = ( summation + target ) // 2
        return getCount(n-1, s1)