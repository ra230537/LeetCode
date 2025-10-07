from typing import Optional
from collections import deque
from tree_utils import create_tree, TreeNode, print_tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
TODO: Como montar uma árvore
TODO: Busca em largura
Não tá no algoritmo mas é importante pesquisar sobre
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node is None:
                continue
            ## Next values to move 
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)

        return root

root = create_tree([4,2,7,1,3,6,9])
new_root = Solution().invertTree(root)
print_tree(new_root)