class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        src_col = image[sr][sc]
        if src_col == color: 
            return image
        
        queue=[(sr, sc)]
        row = len(image)
        col = len(image[0])
        while queue:
            curr= queue.pop(0)
            image[curr[0]][curr[1]] = color

            if (up:=curr[0]-1) >= 0 and src_col == image[up][curr[1]]:
                queue.append((up, curr[1]))

            if (down:=curr[0]+1) < row and src_col == image[down][curr[1]]:
                queue.append((down, curr[1]))

            if (left:=curr[1]-1) >= 0 and src_col == image[curr[0]][left]:
                queue.append((curr[0], left))
            
            if (right:=curr[1]+1) < col and src_col == image[curr[0]][right]:
                queue.append((curr[0], right))

        return image