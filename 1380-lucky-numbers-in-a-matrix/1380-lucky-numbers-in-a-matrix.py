class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        minimum_set=set()
        maximum_set=set()
        for i in range(len(matrix)):
            minimum=float("inf")
            maximum=0
            for j in range(len(matrix[0])):
                if matrix[i][j]<minimum:
                    minimum=matrix[i][j]
            minimum_set.add(minimum)
        for i in range(len(matrix[0])):
            maximum=0
            for j in range(len(matrix)):
                if matrix[j][i]>maximum:
                    maximum=matrix[j][i]
            maximum_set.add(maximum)
        return list(maximum_set.intersection(minimum_set))

        