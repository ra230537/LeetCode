from collections import defaultdict
from typing import List

'''

'''
class Solution:
    
    def get_vertice_number(self, i, m, j):
        return i * m + j
    
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        graph = defaultdict(list)
        visited = set()
        for i in range(n):
            for j in range(m):
                if (grid[i][j] != 1):
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
            nonlocal cur_value
            if node in visited:
                return
            visited.add(node)
            cur_value += 1
            for neighbor in graph[node]:
                dfs(neighbor)
        max_value = 0
        for node in graph.keys():
            cur_value = 0
            if (node in visited):
                continue
            dfs(node)
            max_value = max(max_value, cur_value)
        print(max_value)
        # print(list(visited))
        return max_value
            
Solution().numIslands(
    grid = [
    [0,1,1,0,1],
    [1,0,1,0,1],
    [0,1,1,0,1],
    [0,1,0,0,1]
  ]
)
