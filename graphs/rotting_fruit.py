from typing import List
from collections import deque
'''
Desafio: Fazer usando directions
Como a gente tem uma fonte que propaga alto, isso grita que é uma BFS
Da mesma forma que o problema islands_treasure, a gente precisa pegar todas as frutas podres e ir aplicando a regra em camadas
Qual a regra? Sempre que visitar, torna podre.
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # Primeiro passo: Saber quem são as frutas podres.
        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        # Segundo passo, bfs
        # Global level, é uma variável para controlar quantos niveis a bfs já passou.
        # Na queue, a bfs vai em ondas, então cada nucleo de podridão anda um nivel para a casa ao lado
        # No append, adicionamos a proxima casa e dizemos que a podridão avançou um nivel, não precisa de max porque não vai haver um nivel mais baixo sendo processado
        # depois de um nivel mais baixo pois fazemos ordenadamente
        global_level = 0
        while queue:
            i, j, level = queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (0<=ni<n and 0<=nj<m and grid[ni][nj] == 1):
                    grid[ni][nj] = 2
                    global_level = level + 1
                    queue.append((ni, nj, level + 1))
            print(grid)
            print(global_level)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return global_level
print(Solution().orangesRotting(grid = [[1,1,0],[0,1,1],[0,1,2]]))