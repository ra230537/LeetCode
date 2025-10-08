from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(array, n):
            if n == 1:
                return [array]
            response = []
            for i in range(len(array)):
                # print(array[:i] + array[i+1:])
                permutations = backtrack(array[:i] + array[i+1:], n - 1)
                for i_permut in range(len(permutations)):
                    permutations[i_permut].append(array[i])
                    response.append(permutations[i_permut])
            return response
        return backtrack(nums, len(nums))
print(Solution().permute([1]))
        