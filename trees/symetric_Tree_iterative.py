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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        response = []
        if root == None:
            return response
        queue = deque([(0, root)])
        while queue:
            # print(self.print_queue(queue))
            level, current_node = queue.popleft()
            if current_node != None:
                left_node = current_node.left if current_node != None else None
                right_node = current_node.right if current_node != None else None
                queue.append((level + 1, left_node))
                queue.append((level + 1, right_node))
            current_node_value = current_node.val if current_node != None else None
            if (len(response) == level):
                if (response != []):
                    i = 0
                    j = len(response[-1]) - 1
                    while i < j:
                        if (response[-1][i]!=response[-1][j]):
                            return False
                        i+=1
                        j-=1
                response.append([current_node_value])

            else:
                response[-1].append(current_node_value)
        return True
    def print_queue(self, queue):
        response = []
        for i in queue:
            response.append(i[1].val)
        return response
root = create_tree([1,2,2,None,3,None,3])
print(Solution().isSymmetric(root))