from typing import List
'''
TODO: Observação: Lembrar que
1. O teto é o indice maximo
2. A condição de parada é floor <= ceil e não floor < ceil (Da problema em casos de tamanho 1, por exemplo)
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Primeiro procura dentro dos intervalos da primeira coluna, se for menor . Pode ser que esteja na linha dessa coluna
        Depois faz uma busca binária dentro da linha
        '''
        m = len(matrix)
        n = len(matrix[0])
        # Achar a linha correta
        floor = 0
        ceil = m - 1
        mid = m // 2
        row = 0
        while floor <= ceil:
            if (matrix[mid][0] > target):
                ceil = mid - 1
            elif (matrix[mid][0] <= target):
                row = mid
                floor = mid + 1
            mid = (floor + ceil)//2
        # Achar a coluna correta
        floor = 0
        ceil = n - 1
        mid = n // 2
        while floor <= ceil:
            if (matrix[row][mid] > target):
                ceil = mid - 1
            elif (matrix[row][mid] < target):
                floor = mid + 1
            else:
                return True
            mid = (floor + ceil)//2
        return False
        # Printo linha e coluna
print(Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3))

assert Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3) == True
assert Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=13) == False
assert Solution().searchMatrix(matrix = [[1]], target=1) == True