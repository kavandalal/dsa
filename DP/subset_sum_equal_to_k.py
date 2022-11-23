# PROBLEM - https://www.codingninjas.com/codestudio/problems/subset-sum-equal-to-k_1550954
# REFERENCE - https://www.youtube.com/watch?v=fWX9xDmIzRI&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=15

# DP Recursion
def subsetSumToK(n, k, arr):
    
    dp = [[-1 for _ in range(k+1)] for _ in range(n)] 
    def dfs(ind, target):
        if target == 0 : 
            return True
        if ind == 0: 
            return arr[0] == k
        if dp[ind][target] != -1 : 
            return dp[ind][target]
        
        notTake = dfs(ind - 1 , target )
        take = False
        if arr[ind] <= target : 
          take = dfs(ind - 1 , target - arr[ind])
        dp[ind][target] = take or notTake
        return dp[ind][target]
    
    return dfs(n-1,k)


# DP Tabulation
def subsetSumToK(n, k, arr):
 
    dp = [[False for _ in range(k+1)] for _ in range(n)] 
    for i in range(n):
        dp[i][0]=True
        
    if arr[0] <= k:
        dp[0][arr[0]] = True
    
    for ind in range(1,n):
        for target in range(1,k+1):
            notTake = dp[ind - 1][target]
            take = False
            if arr[ind] <= target : 
                take = dp[ind - 1][target - arr[ind]]
            
            dp[ind][target] = take or notTake
            
    
    return dp[n-1][k]