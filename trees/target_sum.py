# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from tree_utils import TreeNode, create_tree
from typing import Optional
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # response = []
        def dfs(node: TreeNode):
            if (node is None):
                return []
            sub_left = dfs(node.left)
            sub_right = dfs(node.right)
            # print(f'Sub arvore esquerda: {sub_left}, nó atual: {node.val}' )
            # print(f'Sub arvore direita: {sub_right}, nó atual: {node.val}' )
            if (sub_left == [] and sub_right == []):
                return [[node.val]]
            for element in sub_left:
                element.append(node.val + element[-1])
            for element in sub_right:
                element.append(node.val + element[-1])
            # print(sub_left + sub_right)
            return sub_left + sub_right + [[node.val]]
        response = dfs(root)
        count_sum = 0
        for element in response:
            count_sum += element.count(targetSum)
        return count_sum
root = create_tree([10,5,-3,3,2,None,11,3,-2,None,1])
print(Solution().pathSum(root, 8))