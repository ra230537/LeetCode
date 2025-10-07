from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mapping = {}
        for num in nums:
            if num not in mapping:
                mapping[num] = 0
            mapping[num]+=1
        for num, count in mapping.items():
            if count == 1:
                return num
        

assert Solution().singleNumber(nums = [2,2,4,2, 1, 1, 1]) == 4
assert Solution().singleNumber(nums = [99,2,2,2,1,1,1]) == 99