from typing import List
from collections import defaultdict, deque
'''
- lista de pre reqs [a, b] em que b precisa ser feito antes de a
- num curses vai me dizer quantos existem de 0 a num - 1
- A ideia é obviamente fazer uma busca topologica
- cada indice vai ser um nó
- vamos salvar o g-in em numa lista eai poderemos modificar o in em o(1)
- vamos fazer uma lista de adjacencias para conectar os grafos
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        # Indice é o node, valor é a quantidade de graus de entrada
        in_degree = [0] * numCourses
        queue = deque()
        response = []
        for pre in prerequisites:
            first = pre[1]
            second = pre[0]
            graph[first].append(second)
            in_degree[second]+=1
        # Aqui temos que lembrar que o in_degree é uma lista cujos nos são o indice e o grau o valor, então caso o valor seja 0, adicionamos o nó correspondente.        
        for node, degree in enumerate(in_degree):
            if degree == 0:
                queue.append(node)
        while queue:
            node = queue.popleft()
            response.append(node)
            for neighbor_node in graph[node]:
                # Reduz um grau de entrada de todos os vizinhos
                in_degree[neighbor_node] -= 1
                print(in_degree)
                # Se o grau agora é 0 ele precisa ser processado.
                if (in_degree[neighbor_node] == 0):
                    queue.append(neighbor_node)
        if (sum(in_degree) > 0):
            return False
        return True
print(Solution().canFinish(numCourses = 2, prerequisites = [[0,1]]))