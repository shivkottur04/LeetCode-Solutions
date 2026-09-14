class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        nums=[]
        for i in range(len(matrix[0])):
            a=[]
            for j in range(len(matrix)):
                a.append(matrix[j][i])
            nums.append(a)     
        return nums