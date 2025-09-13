# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
TODO: Busca em profundidade

'''
from typing import List, Optional
from tree_utils import TreeNode, create_tree
class Solution:
    total = 0
    def get_sum(self, root: Optional[TreeNode], path: List[int]):
        left_node = root.left
        right_node = root.right
        if left_node is None and right_node is None:
            count = 0
            for idx in range(len(path)-1,-1,-1):
                count += path[idx] * 10 ** (len(path) - idx - 1)
            print(count)
            self.total += count
            return None
        elif left_node is None:
            right_path = path.copy()
            right_node and right_path.append(right_node.val)
            self.get_sum(right_node, right_path)
            return None
        elif right_node is None:
            left_path = path.copy()
            left_node and left_path.append(left_node.val)
            self.get_sum(left_node, left_path)
            return None

        left_path = path.copy()
        left_node and left_path.append(left_node.val)
        self.get_sum(left_node, left_path)

        right_path = path.copy()
        right_node and right_path.append(right_node.val)
        self.get_sum(right_node, right_path)

        return None

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.get_sum(root, [root.val])
        return self.total
node = create_tree([4,9,0,None,1])
print(Solution().sumNumbers(node))