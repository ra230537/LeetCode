from typing import Optional
from tree_utils import create_tree, TreeNode
class Solution:
    '''
    Aprendizado: essas variaveis globais a gente não passa dentro da função, fica confuso.
    O pulo do gato dessa solução é pensar o seguinte:
        Quando vamos para a esquerda o limite superior é o valor atual e o limite inferior permanece o mesmo antigo
        Da mesma forma acontece com o da direita
    '''
    valid_bst = True
    def get_valid_bst(self, root: TreeNode, inferior_limit, superior_limit):
        if (root == None):
            return 
        
        left_node = root.left
        right_node = root.right
        if (right_node != None and right_node.val <= root.val) or \
            (left_node != None and left_node.val >= root.val):
            self.valid_bst = False
        if ((superior_limit != None and root.val >= superior_limit) or \
            (inferior_limit != None and root.val <= inferior_limit) ):
            self.valid_bst = False
        
        self.get_valid_bst(root.left, inferior_limit, root.val)
        self.get_valid_bst(root.right,root.val, superior_limit)
        return 
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.get_valid_bst(root, None, None)
        return self.valid_bst

root = create_tree([5,4,6,None,None,3,7])
print(Solution().isValidBST(root))