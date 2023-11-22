from collections import defaultdict

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)

        m , n = len(mat), len( mat[0])
        for i in range(m): 
            for j in range ( n):
                d[i-j].append(mat[i][j])

        for k in d:
            d[k].sort( reverse=True)

        for i in range(m) :
            for j in range(n):
                mat[i][j] = d[i-j].pop()

        return mat