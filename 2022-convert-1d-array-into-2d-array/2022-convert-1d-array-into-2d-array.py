class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        lst=[[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                lst[i][j]=original.pop(0)
        return lst