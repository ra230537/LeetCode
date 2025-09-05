from typing import List
class Solution:
    def count_cells(self, i, j, m, n, matrix):
        counter = 0
        for row in range(max(0, i-1), min(m, i + 2)):
            for col in range(max(0, j - 1), min(n, j + 2)):
                if (i == row and j == col):
                    continue
                if (abs(matrix[row][col]) == 1):
                    counter += 1
        return counter
    '''
    Uma estratégia é atribuir -1 a um valor vivo que morreu e 2 a um valor morto que viveu
    Guardam duas infomráco~es ao mesmo tempo: Estado original da celula e o seu proximo estado
    0 -> Morto -> Morto
    1 -> vivo -> vivo
    2 -> Morto ->  vivo
    -1 -> Vivo -> Morto

    Dai sabemos quem estava vivo nessa parte, bastaria contar quem tinha valor -1 ou 1, sempre que encontrarmos -1 ou 1 somamos um no contador
    '''
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Regras
        1. Celula viva com menos que dois vivos ao lado, morre
        
        1. Se Celula = 1 & Contador_celulas_vivas(celula) < 2      => celula = 0
        2. Se Celula = 1 & Contador_celulas_vivas(celula) == 2 | 3 => Celula = 1
        3. Se Celula = 1 & Contador_celulas_vivas(celula) > 3      => Celula = 0
        4. Se Celula = 0 & Contador_celulas_vivas(celula) == 3     => Celula = 1
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                side_count = self.count_cells(i, j, m, n, board)
                if (board[i][j] == 1 and side_count < 2):
                    board[i][j] = -1
                
                elif (board[i][j] == 1 and (side_count == 2 or side_count == 3)):
                    board[i][j] = 1
                
                elif (board[i][j] == 1 and side_count > 3):
                    board[i][j] = -1

                elif (board[i][j] == 0 and side_count == 3):
                    board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if (board[i][j] == 2):
                    board[i][j] = 1
                elif(board[i][j] == -1):
                    board[i][j] = 0
        return board
print(Solution().gameOfLife(board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))