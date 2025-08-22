# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from tree_utils import create_tree, TreeNode
class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if (root == None):
            return False
        if (root.left == None and root.right == None):
            return targetSum == root.val
        has_left_sum = self.hasPathSum(root.left, targetSum - root.val)
        has_right_sum = self.hasPathSum(root.right, targetSum - root.val)
        return has_left_sum or has_right_sum
root = create_tree([])
print(Solution().hasPathSum(root, 0))