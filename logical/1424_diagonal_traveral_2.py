# https://www.youtube.com/watch?v=k4YsQgeJBt0
# https://leetcode.com/problems/diagonal-traverse-ii/

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        v= [] 
        for i in range(len(nums)): 
            for j in range ( len ( nums[i])): 
                v.append( ( i+j , j , nums[i][j]))

        ans = list( x[2] for x in sorted(v))
        return ans
    

