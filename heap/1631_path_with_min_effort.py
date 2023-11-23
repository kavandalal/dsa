# https://www.youtube.com/watch?v=0ytpZyiZFhA
# https://leetcode.com/problems/path-with-minimum-effort/description/
# used min heaq to find the soution, dijitras algorithm

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights : 
            return 0
        
        row,col = len( heights ), len( heights[0] )
        maxi = 0 # until now
        visited = set()
        heap = [(0,0,0)] # effort, row, col
        
        while heap:
            effort, rowHere, colHere = heapq.heappop(heap)
            maxi = max( effort , maxi )

            if ( rowHere , colHere ) == ( row-1 , col-1): 
                return maxi
            
            visited.add( (  rowHere, colHere ) )
            move = [(-1,0), (0,1),(1,0), ( 0,-1)]
            for dr , dc in move: 
                newRow , newCol = rowHere + dr , colHere + dc
                
                if 0<=newRow<row and 0 <= newCol < col and ( newRow, newCol ) not in visited: 
                    newEffort =  abs( heights[rowHere][colHere] - heights[newRow][newCol])
                    heapq.heappush(heap , (newEffort,newRow,newCol ))
            
        return maxi


