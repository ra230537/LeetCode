from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx_ceil = len(nums)-1
        idx_floor = 0
        idx_mid = (idx_ceil + idx_floor) // 2
        last_idx = idx_mid
        while idx_floor <= idx_ceil:
            if (nums[idx_mid] == target):
                return idx_mid
            if (nums[idx_mid] > target):
                idx_ceil = idx_mid - 1
            else:
                idx_floor = idx_mid + 1
            last_idx = idx_mid
            idx_mid = (idx_ceil + idx_floor) // 2
        if (nums[last_idx] > target):
            return last_idx
        else:
            return last_idx + 1
print(Solution().searchInsert(nums = [1,3,5,6], target = 6))