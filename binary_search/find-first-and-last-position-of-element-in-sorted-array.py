from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        bot = 0
        top = len(nums)-1
        mid = (bot + top) // 2
        first_ocurrence_idx = -1
        while bot <= top:
            if (target > nums[mid]):
                bot = mid + 1
            elif (target < nums[mid]):
                top = mid - 1
            else:
                first_ocurrence_idx = mid
                break
            mid = (bot + top) // 2

        if (first_ocurrence_idx == - 1):
            return [-1, -1]

        bot = 0
        top = first_ocurrence_idx - 1
        mid = (bot + top) // 2
        first_idx = -1
        while bot <= top:
            if (target > nums[mid]):
                bot = mid + 1
            elif (target == nums[mid]):
                top = mid - 1
                first_idx = mid
            mid = (bot + top) // 2

        bot = first_ocurrence_idx+1
        top = len(nums)-1
        mid = (bot + top) // 2
        second_idx = -1
        while bot <= top:
            if (target == nums[mid]):
                bot = mid + 1
                second_idx = mid
            elif (target < nums[mid]):
                top = mid - 1
            mid = (bot + top) // 2
        print([first_idx, first_ocurrence_idx, second_idx])
        if (first_idx == -1 and second_idx == -1):
            return [first_ocurrence_idx, first_ocurrence_idx]
        elif (first_idx == -1):
            return [first_ocurrence_idx, second_idx]
        elif (second_idx == -1):
            return [first_idx, first_ocurrence_idx]
        else:
            return [first_idx, second_idx]

assert Solution().searchRange(nums = [5,7,7,8,8,10], target = 8) == [3, 4]
assert Solution().searchRange(nums = [5,7,7,8,8,10], target = 6) == [-1,-1]
assert Solution().searchRange(nums = [], target = 0) == [-1,-1]
assert Solution().searchRange(nums = [5,7,8,8,8,8], target = 8) == [2,5]