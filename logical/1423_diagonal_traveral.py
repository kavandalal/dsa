# Self
# https://leetcode.com/problems/diagonal-traverse/

#  if the addition of row + col is odd then store row number else store col, then sort will give correect result
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        v = [] 
        for i in range( len ( mat)): 
            for j in range ( len ( mat[i])):
                odd = (i + j) % 2 != 0 
                v.append(( i + j , i if odd else j , mat[i][j]))

        ans = list( x[2] for x in sorted ( v) )
        return ans

