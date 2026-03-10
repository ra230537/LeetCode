from typing import List
from collections import deque
'''
TODO: A sacada aqui eh que no bfs a gente vai ter ondas, no primeiro while a gente vai rodar
Só quem tá a distância 1 do nivel 0, depois vai adicionar quem tá na distancia 2
Dai vai rodar a distancia 2 dentro do while e assim por diante,
como estamos partindo sempre do menor nivel pro maior, garantidamente o primeiro valor
a preencher o grid vai ser o menor possível.

Essa estratégia de directions é boa quando temos grid
'''
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        INF = 2147483647
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    queue.append((i, j))
        # Roda a primeira camada
        while queue:
            i, j = queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == INF:
                    grid[ni][nj] = grid[i][j] + 1
                    # Adiciona o nível 2
                    queue.append((ni, nj))

        return grid