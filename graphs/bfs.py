from collections import defaultdict, deque
'''
No bfs a gente vai visitar os nós em camadas, ou seja, primeiro visitamos o nó inicial, 
depois todos os seus vizinhos, 
depois os vizinhos dos vizinhos, e assim por diante. 
Para isso, usamos uma fila (queue) para manter a ordem de visitação dos nós.
'''
def bfs_template(edges, start_node):
    # 1. Construir o grafo
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # 2. Inicializar a fila e o conjunto de visitados
    queue = deque([start_node])
    visited = {start_node} # Já adicionamos o nó inicial para evitar reprocessamento

    # 3. Loop principal
    while queue:
        # Quantidade de nós no nível atual (útil para contar distância/camadas)
        level_size = len(queue)
        print(f"Nível atual: {level_size} nós")
        
        for _ in range(level_size):
            node = queue.popleft()
            print(f"Visitando: {node}")
            
            # Adiciona vizinhos não visitados na fila
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
bfs_template([(1, 2), (1, 3), (2, 4), (3, 4)], 1)