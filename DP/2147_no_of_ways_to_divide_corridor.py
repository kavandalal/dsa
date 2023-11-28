# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

class Solution:
    # DP this does not work for "SPSPPSSPSSSS" case
    def numberOfWays1(self, corridor: str) -> int:
        MOD = 10**9 + 7
        n = len ( corridor )
        mem = [[-1] * 3]* n # n X 3, 3 for number of seats(0/1/2)
        def dfs(i, seats):
            if i == n: 
                return 1 if seats == 2 else 0 

            if mem[i][seats] != -1:
                return  mem[i][seats]
            res = 0 
            if seats == 2 :
                if corridor[i] == 'S': 
                    res = dfs(i + 1,1)
                else: 
                     res = dfs(i + 1,2) + dfs(i + 1,0)
            else: 
                if corridor[i] == 'S': 
                    res = dfs(i +1, seats+1)
                else: 
                    res = dfs(i+1 , seats)
                
            mem[i][seats] = res % MOD
            return mem[i][seats]
        
        return dfs(0,0)
    
    # other thought where we will just collect the postion of "S" and then get combination of all the places left between each "S"
    # https://youtu.be/YOTjCd4Eyhc?si=K6BYQ_qrmdQPKVlH&t=1155 
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        sPlace = []
        
        for i,v in enumerate(corridor): 
            if v == 'S': 
                sPlace.append(i)

        n = len ( sPlace )
        if n % 2 != 0 or n < 2 : 
            return 0 
        i = 1
        res = 1
        while i < n-1:
            res *= sPlace[i+1] - sPlace[i]
            i+=2

        return res % MOD 

        