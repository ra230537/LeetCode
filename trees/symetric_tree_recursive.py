from typing import Optional
from tree_utils import create_tree, TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self, left: Optional[TreeNode],right: Optional[TreeNode]):
        if left == None and right == None:
            return True
        if left != None or right != None or left.val != right.val:
            return False
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root == None:
            return True
        return self.isMirror(root.left, root.right)
    
root = create_tree([1,2,2,None,3,None,3])
print(Solution().isSymmetric(root))