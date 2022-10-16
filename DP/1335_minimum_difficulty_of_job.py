# LINK https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/discuss/490316/JavaC%2B%2BPython3-DP-O(nd)-Solution

class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n: 
            return -1
        dp = [[-1 for j in range(n)] for i in range(d+1)]
        
        def backtrack(day , idx):
            if day == 1: 
                return max(jobDifficulty[idx: ])
                
            if dp[day][idx] != -1: 
                return dp[day][idx]
            
            maxHere = 0 
            sumHere = float('inf')
            
            for i in range(idx, n-day+1): 
                maxHere = max (maxHere ,jobDifficulty[i])
                sumHere = min (sumHere ,maxHere + backtrack(day-1 ,i+1))
                
            dp[day][idx] = sumHere
            return sumHere
        
        return backtrack(d, 0)
                

