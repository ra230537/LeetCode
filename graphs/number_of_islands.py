from collections import defaultdict, deque
from typing import List

'''
TODO: Dica, lembra que pra indexar uma matriz é só multiplicar indice da linha * numero de colunas + indice da coluna
É como se a gente tivesse enfileirando as matrizes

Essa questão não tem muito segredo, Basicamente é montar o grafo e fazer um dfs comum
O unico ponto que provavelmente é simples mas que eu não lembrava eh que precisa ter um laço for por fora do dfs pra garantir que
a gente pegue partes não conectadas do grafo.
'''
class Solution:
    
    def get_vertice_number(self, i, m, j):
        return i * m + j
    
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        graph = defaultdict(list)
        visited = set()
        for i in range(n):
            for j in range(m):
                if (grid[i][j] != "1"):
                    continue
                u = self.get_vertice_number(i, m, j)
                graph[u].append(u)
                if (i < n - 1 and grid[i][j] == grid[i+1][j]):
                    v = self.get_vertice_number(i + 1, m, j)
                    graph[u].append(v)
                    graph[v].append(u)
                if (j < m - 1 and grid[i][j] == grid[i][j+1]):
                    v = self.get_vertice_number(i, m, j + 1)
                    graph[u].append(v)
                    graph[v].append(u)
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
        response = 0
        for node in graph.keys():
            if (node in visited):
                continue
            response+=1
            dfs(node)
        # print(response)
        # print(list(visited))
        return response
            
Solution().numIslands(
    grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
)
