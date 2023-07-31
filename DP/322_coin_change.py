# 322 LEETCODE Coin Change
# https://www.youtube.com/watch?v=myPeWb3Y68A&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=21
# https://leetcode.com/problems/coin-change/

class Solution:
    
    # Memorisation
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)
        mem = [[-1 for _ in range(amount+1)] for _ in range(n)]
        def rec(ind, target) -> int:
            if ind == 0 : 
                if target % coins[0] == 0: 
                    return target // coins[ind] 
                return 1e9 
            if mem[ind][target] != -1:
                return mem[ind][target] 
            
            notTake = 0 + rec(ind-1, target)
            take = float('inf')
            if coins[ind] <= target: 
                take = 1 + rec(ind, target - coins[ind])
            
            mem[ind][target] = min(take, notTake)
            return mem[ind][target]
        
        ans = rec(n-1, amount)
        return -1 if ans>= 1e9 else ans
    # Tabulation
    def coinChange2(self, coins: list[int], amount: int) -> int:
        n = len(coins)
        mem = [[0 for _ in range(amount+1)] for _ in range(n)]

        for i in range(amount+1) : 
            if i % coins[0] == 0 :
                mem[0][i] = i // coins[0]
            else : 
                mem[0][i] = 1e9

        for ind in range(1,n ): 
            for target in range(amount+1):
                notTake = 0 + mem[ind-1][target]
                take = float('inf')
                if coins[ind] <= target: 
                    take = 1 + mem[ind][target - coins[ind]]
                
                mem[ind][target] = min(take, notTake)
        ans = mem[n-1][amount]
        return -1 if ans>= 1e9 else ans
    
    # space optimisation
    def coinChange3(self, coins: list[int], amount: int) -> int:
        n = len(coins)
        prev = [0] * (amount+1)
        cur = [0] * (amount+1)

        for i in range(amount+1) : 
            if i % coins[0] == 0 :
                prev[i] = i // coins[0]
            else : 
                prev[i] = 1e9

        for ind in range(1,n ): 
            for target in range(amount+1):
                notTake = 0 + prev[target]
                take = float('inf')
                if coins[ind] <= target: 
                    take = 1 + cur[target - coins[ind]]
                
                cur[target] = min(take, notTake)
            prev = cur
        ans = prev[amount]
        return -1 if ans>= 1e9 else ans



if __name__ == '__main__':
    x = Solution()
    coins = [1,2,5]
    amount = 11
    print ( x.solve(coins, amount))
