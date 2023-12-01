# https://leetcode.com/problems/detect-cycles-in-2d-grid/description/

from collections import deque
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        s={}
        
        m=len(grid)
        n=len(grid[0])

        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        def helper(i,j):
            char=grid[i][j]
            q=deque()
            q.append((i,j,-1,-1))
            while(q):
                x,y,c,d=q.popleft()
                if(0<=x<m and 0<=y<n and grid[x][y]==char):
                    if((x,y) not in s):
                        s[(x,y)]=(c,d)
                        for dirR, dirC in dir: 
                            newR , newC = x + dirR , y + dirC
                            if (newR,newC) != (c,d):
                                q.append((newR,newC,x,y))    
                    elif(s[(x,y)]!=(c,d)):
                        return True
            return False
            


        for i in range(0,m):
            for j in range(0,n):
                if((i,j) not in s):
                    if(helper(i,j)):
                        return True
        return False