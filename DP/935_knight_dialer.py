class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 10

        MOD = 10**9 + 7 

        valid = [(0,0), (0,1),(0,2),(1,0), (1,1),(1,2),(2,0), (2,1),(2,2),(3,1)]
        def isValid(x , y): 
            return (x,y) in valid
        
        moves = [(1,2),(1,-2),(-1,2), (-1,-2),(2,1),(-2,1),(2,-1), (-2,-1)]
        # memory = [[[-1]*n]*10]*10

        @lru_cache(None)
        def dp(x , y, steps): 
            if steps == 0: 
                return 1
            
            # if memory[x][y][steps] != -1:
            #     return memory[x][y][steps]
            
            comb = 0
            for i,j in moves:
                calcI , calcJ = x + i , y + j  
                if isValid(calcI,calcJ): 
                    comb += dp(calcI, calcJ ,steps - 1)
            
            # memory[x][y][steps] = comb 
            return comb % MOD
        
        combParent = 0
        for i , j in valid:
            combParent += dp(i,j,n-1)
        
        return combParent % MOD