# https://leetcode.com/problems/rotting-oranges/description/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len( grid )
        m = len( grid[0] )
        visited =  [[0] * m for j in range( n ) ] 
        queue = []
        countFresh = 0
        for i in range( n ): 
            for j in range( m ): 
                if grid[i][j] == 2: 
                    queue.append( (0,i,j) )
                    visited[i][j] = 2


                if grid[i][j] == 1: 
                    countFresh += 1 
        
        maxTime = 0
        pathR = [-1,0,1,0]
        pathC = [0,1,0,-1]
        visitedFresh = 0 
        while len(queue) != 0:
            current = queue.pop(0)
            time, x , y = current[0], current[1], current[2] 
            maxTime = max(maxTime, time)
            for i in range(4): 
                newRow = x + pathR[i]
                newCol = y + pathC[i]
                if 0<=newRow<n and 0<=newCol<m and visited[newRow][newCol] == 0 and grid[newRow][newCol] == 1: 
                    queue.append( ( time + 1 , newRow, newCol ) )
                    visited[newRow][newCol] = 2 
                    visitedFresh += 1
        
        if countFresh != visitedFresh  :
            return -1 

        return maxTime