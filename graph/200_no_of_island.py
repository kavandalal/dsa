class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len( grid )
        col = len( grid[0] )
        visited= set()

        def dfs(x, y ): 
            visited.add( (x,y))
            for i , j in [(1,0), (-1,0), (0,-1), (0,1)]:
                new_x , new_y = x + i , y+ j
                if 0<=new_x<row and 0<=new_y<col and (new_x,new_y) not in  visited and grid[new_x][new_y] == "1":
                    dfs(new_x,new_y)
                

        counter = 0 
        for i in range(row): 
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in visited: 
                    counter += 1
                    dfs(i,j)
        
        return counter