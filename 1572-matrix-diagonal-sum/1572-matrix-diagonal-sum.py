class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        sums=0
        for i in range(0,n):
            for j in range(0,n):
                if i==j:
                    sums+=mat[i][j]
                elif i != j and i+j==n-1:
                    sums+=mat[i][j]
        return sums