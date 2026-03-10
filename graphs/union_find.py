class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Rank ajuda a manter a árvore achatada (otimização)
        self.rank = [1] * size 

    def find(self, x):
        # Path compression: aponta o nó direto para a raiz
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            # Union by rank: anexa a árvore menor na raiz da árvore maior
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            return True # Retorna True se houve uma união (não estavam no mesmo grupo)
        return False # Retorna False se já estavam conectados (útil para achar ciclos)