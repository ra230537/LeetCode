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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree_1 = []
        lista = deque()
        lista.append(p)
        while len(lista) > 0:
            node = lista.popleft()
            if node is None:
                tree_1.append(None)
                continue
            tree_1.append(node.val)
            lista.append(node.left)
            lista.append(node.right)

        tree_2 = []
        lista = deque()
        lista.append(q)
        while len(lista) > 0:
            node = lista.popleft()
            if node is None:
                tree_2.append(None)
                continue
            tree_2.append(node.val)
            lista.append(node.left)
            lista.append(node.right)
        if len(tree_2) != len(tree_1):
            return False
        else:
            for idx in range(len(tree_1)):
                if tree_1[idx] != tree_2[idx]:
                    return False
        return True
p = create_tree([1, 2])
q = create_tree([1, None, 2])
print(Solution().isSameTree(p, q))