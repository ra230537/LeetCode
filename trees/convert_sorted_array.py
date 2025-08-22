# Definition for a binary tree node.
from typing import List, Optional
from tree_utils import TreeNode
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if (len(nums) == 0):
            return None
        if (len(nums) == 1):
            return TreeNode(nums[0])
        
        center_idx = len(nums)// 2
        center_value = nums[center_idx]
        center_node = TreeNode(center_value)
        
        right_array = nums[center_idx+1:len(nums)]
        center_node.right = self.sortedArrayToBST(right_array)
        
        left_array = nums[0:center_idx]
        center_node.left = self.sortedArrayToBST(left_array)
        return center_node

print(Solution().sortedArrayToBST(nums = [-10,-3,0,5,9]))