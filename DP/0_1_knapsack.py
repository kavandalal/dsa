# 0/1 Knapsack 
# https://www.youtube.com/watch?v=GqOmJHQZivw&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=20
# https://www.codingninjas.com/studio/problems/0-1-knapsack_920542?leftPanelTab=1

class Solution:
    # Recursion 
    def solve(self , w : list ,val : list,maxWt :int) -> int:

        def rec(ind,wt) -> int:
            if ind == 0: 
                if wt >= w[0]: return val[0] 
                else: return 0
            
            notTake = 0 + rec(ind-1, wt)
            take = float('-inf')
            if w[ind] <= wt: 
                take = w[ind] + rec(ind-1, wt - w[ind])

            return max(take , notTake)
        
        n = len(w)
        return rec(n-1, maxWt)

    # Memorisation
    def solve2(self , w : list ,val : list,maxWt :int) -> int:
        n = len(w)
        mem = [[-1 for i in range(maxWt+1)] for j in range(n)]
        def rec(ind,wt) -> int:
            if ind == 0: 
                if wt >= w[0]: return val[0] 
                else: return 0
            if mem[ind][wt] != -1: 
                return mem[ind][wt]
            
            notTake = 0 + rec(ind-1, wt)
            take = 0
            if w[ind] <= wt: 
                take = val[ind] + rec(ind-1, wt - w[ind])

            mem[ind][wt] = max(take , notTake)
            return mem[ind][wt] 
        
        return rec(n-1, maxWt) 
    
    # Tabulation
    def solve3 (self , w : list ,val : list,maxWt :int) -> int:
        n = len(w)
        prev = [0] * (maxWt+1)
        cur = [0] * (maxWt+1)

        for i in range(w[0],maxWt): 
            prev[i] = val[0]
        
        for ind in range(1,n): 
            for wt in range(maxWt+1): 
                notTake = 0 + prev[wt]
                take = 0
                if w[ind] <= wt: 
                    take = val[ind] + prev[ wt - w[ind]]

                cur[wt] = max(take , notTake)
            prev = cur
        
        return prev[maxWt]



        


if __name__ == '__main__':
    x = Solution()
    w = [3 , 2 , 5]
    val = [30, 40 , 60]
    maxWt = 6
    print ( x.solve(w,val, maxWt))
