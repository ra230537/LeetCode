from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict_compare = {}
        for idx, num in enumerate(nums):
            if num not in dict_compare:
                dict_compare[num] = idx
            else:
                # Basta comparar o atual com o anterior
                diff = idx - dict_compare[num]
                if (diff <= k):
                    return True
                else:
                    # Guarda a ultima posicao
                    dict_compare[num] = idx
        return False
print(Solution().containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
