# Definition for a binary tree node.
from collections import deque
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(nums: List[Optional[int]]) -> Optional[TreeNode]:
        """
        Cria uma árvore binária a partir de uma lista em ordem de nível.
        'None' na lista representa um nó nulo.
        """
        # 1. Caso inicial: se a lista estiver vazia, não há árvore.
        if not nums:
            return None

        # 2. O primeiro elemento da lista é sempre a raiz da árvore.
        root = TreeNode(nums[0])
        
        # 3. Usamos uma fila (deque é uma implementação otimizada de fila)
        #    para guardar os nós que ainda precisam ter seus filhos adicionados.
        #    Começamos com a raiz na fila.
        queue = deque([root])
        
        # 4. Usamos um índice 'i' para percorrer a lista 'nums'.
        #    Começamos em 1, pois o elemento 0 já foi usado para a raiz.
        i = 1

        # 5. O loop continua enquanto houver nós na fila para processar.
        while queue:
            # Pega o próximo nó da fila (o mais antigo). Este será o "pai".
            current_node = queue.popleft()

            # 6. Tenta adicionar o filho da ESQUERDA.
            # Verifica se nosso índice ainda está dentro da lista.
            if i < len(nums):
                # Se o valor na lista não for None, criamos o nó filho.
                if nums[i] is not None:
                    left_child = TreeNode(nums[i])
                    current_node.left = left_child
                    # Adicionamos o novo filho na fila para que ele também
                    # possa ter seus próprios filhos no futuro.
                    queue.append(left_child)
                # Avançamos o índice para o próximo elemento da lista.
                i += 1

            # 7. Tenta adicionar o filho da DIREITA.
            # O processo é idêntico ao da esquerda.
            if i < len(nums):
                if nums[i] is not None:
                    right_child = TreeNode(nums[i])
                    current_node.right = right_child
                    # Adicionamos o filho direito na fila.
                    queue.append(right_child)
                # Avançamos o índice novamente.
                i += 1

        # 8. Ao final do loop, a árvore está toda conectada. Retornamos a raiz.
        return root

def print_tree(p: Optional[TreeNode]):
    output = []
    lista = deque([p])
    while lista:
        node = lista.popleft()
        if node is None:
            continue
        output.append(node.val)
        lista.append(node.left)
        lista.append(node.right)
    print(output)