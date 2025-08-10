# Definition for a binary tree node.
from collections import deque
from typing import List, Optional
from tree_utils import TreeNode, create_tree
class Solution:
    # def __init__(self):
    max_depth = 0
    def dfs(self, root: TreeNode, current_depth):
        if root == None:
            return 
        current_depth += 1
        if (current_depth > self.max_depth):
            self.max_depth = current_depth
        self.dfs(root.left, current_depth)
        self.dfs(root.right, current_depth)
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Eu vou fazer uma busca em profundidade
        '''
        self.dfs(root, 0)
        return self.max_depth

    
root = create_tree([1,None,2])
print(Solution().maxDepth(root))