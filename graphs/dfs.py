from collections import defaultdict
'''
No dfs a gente vai visitar os nós em profundidade, ou seja, primeiro visitamos o nó inicial, 
depois seguimos por um caminho até o final, e então voltamos para explorar outros caminhos.
Para isso, usamos uma pilha (stack) ou recursão para manter a ordem de visitação dos nós.
'''
def dfs_template(edges, start_node):
    # 1. Construir o grafo (Lista de Adjacência)
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u) # Se for grafo não-direcionado

    visited = set()

    # 2. Definir a função recursiva
    def dfs(node):
        if node in visited:
            return
        
        # Marca como visitado e processa o nó
        visited.add(node)
        print(f"Visitando: {node}")

        # Visita os vizinhos
        for neighbor in graph[node]:
            dfs(neighbor)

    # 3. Chamar a função a partir do nó inicial
    dfs(start_node)
    
dfs_template([(1, 2), (1, 3), (2, 4), (3, 4)], 1)