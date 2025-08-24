from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if (len(nums) == 0):
            return []
        response = []
        current_range = f"{nums[0]}"
        for idx in range(1, len(nums)):
                if (nums[idx] - nums[idx-1] == 1):
                    if ( '>' in current_range):
                        range_list = current_range.split('->')
                        range_list[-1] = str(nums[idx])
                        current_range = '->'.join(range_list)
                    else:
                        current_range+= f"->{str(nums[idx])}"
                else:
                    response.append(current_range)
                    current_range = f"{nums[idx]}"
        response.append(current_range)
        return response
print(Solution().summaryRanges(nums = [0,2,3,4,6,8,9]))