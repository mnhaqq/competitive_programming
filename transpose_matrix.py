class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed = []

        i = 0
        while i < len(matrix[0]):
            add = []
            j = 0
            while j < len(matrix):
                add.append(matrix[j][i])
                j+=1
            i+=1
            transposed.append(add)
        return transposed