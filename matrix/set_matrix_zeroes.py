from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Mapeando as colunas e as linhas e ir modificando para 0
        """
        map_i = {}
        map_j = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (matrix[i][j] == 0):
                    map_i[i] = True
                    map_j[j] = True
        for row_idx in map_i.keys():
            for column_idx in range(len(matrix[0])):
                matrix[row_idx][column_idx] = 0
        for column_idx in map_j.keys():
            for row_idx in range(len(matrix)):
                matrix[row_idx][column_idx] = 0
        return matrix