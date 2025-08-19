from typing import Optional, List
from tree_utils import create_tree, TreeNode
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Acho que é so fazer uma busca em largura mas como fazemos isso?
        usando uma fila
        ter uma lista de resposta vazia
        o primeiro item da fila é root
        enquanto a fila não estiver vazia
        adiciona o filho da esquerda e depois o da direita, adiciona uma tupla (level, valor)
        ter uma variavel de controle para verificar o tamanho da fila, dai 
        se o valor do level for maior que o tamanho da fila, nós damos append com um nivel a mais
        se ele for igual, so adiicionamos um item no ultimo lugar da fila
        '''
        response = []
        if root == None:
            return response
        queue = deque([(0, root)])
        while queue:
            # print(self.print_queue(queue))
            level, current_node = queue.popleft()
            if(current_node.left != None):
                queue.append((level + 1, current_node.left))
                # print(current_node.left.val)
            if (current_node.right != None):
                queue.append((level + 1, current_node.right))
                # print(current_node.right.val)
            if (len(response) == level):
                response.append([current_node.val])
            else:
                response[-1].append(current_node.val)
        return response
    def print_queue(self, queue):
        response = []
        for i in queue:
            response.append(i[1].val)
        return response
root = create_tree([3,9,20,None,None,15,7])
print(Solution().levelOrder(root))