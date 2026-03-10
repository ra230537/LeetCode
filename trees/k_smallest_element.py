from typing import Optional
from tree_utils import create_tree, TreeNode
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
Eu acredito que a sacada do problema seja se aproveitar da dfs em uma árvore
'''



class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        level = 0
        response_node = None
        def dfs(node: TreeNode):
            nonlocal level
            nonlocal response_node
            # processar, dessa forma eu não preciso me preocupar com nulos na hora de ver os filhos
            if node is None:
                return
            # Já achei o meu response node, eu não preciso mais percorrer nada
            if response_node is not None:
                return
            # Percorro o nó filho
            dfs(node.left)
            
            # Processo o nó atual depois de pegar o filho in-order (se fosse pré seria antes do left e se fosse pós seria depois do right)
            level += 1
            if(k == level):
                response_node = node.val
                return
            # Processo o nó direito
            dfs(node.right)
        dfs(root)
        return response_node
    '''
    TODO: Uma abordagem mais fácil seria fazer a um vetor inorder e pegar o k-1 do vetor gerado
    '''
    def kthSmallestv2(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root: TreeNode):
            if (root is None):
                return []
            left_subtree = inorder(root.left)
            current_node = [root.val]
            right_subtree = inorder(root.right)
            return left_subtree + current_node + right_subtree
        return inorder(root)[k-1]
    '''
    Notas: Se eu quisesse uma preOrder ou uma posOrder bastaria colocar o current_node como primeiro elemento da soma ou como ultimo para alcançar as ordenações
    respectivamente
    Pre-order: return current_node + left_subtree + right_subtree
    pos-order: return left_subtree + right_subtree + current_node
    '''
    
root = create_tree([5,3,6,2,4,None,None,1])
print(Solution().kthSmallest(root, 3))

