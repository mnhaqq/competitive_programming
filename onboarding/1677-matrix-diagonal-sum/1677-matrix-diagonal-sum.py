class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        matrix_size = len(mat)
        sum = 0

        i = primary = 0
        secondary = matrix_size - 1
        while i < matrix_size:
            if primary == secondary:
                sum += mat[i][primary]
            else:
                sum += mat[i][primary] + mat[i][secondary]
            primary += 1
            secondary -= 1
            i += 1
        return sum