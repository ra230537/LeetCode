from typing import List, Set

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        response = [[]]
        current_max_size = 0
        current_size = len(nums)
        while current_max_size <= current_size:
            buffer = []
            for i in nums:
                for sub_set_idx in range(len(response)-1,-1,-1):
                    current_sub_set = set(response[sub_set_idx].copy())
                    # print(f'Meu subset atual eh {current_sub_set}')
                    # não quero pegar valores menores do que oque eu estou analisando agora para não haver duplicidade
                    if len(current_sub_set) < current_max_size:
                        break 
                    #o(logn)
                    if i not in current_sub_set:
                        current_sub_set.add(i)
                        if current_sub_set not in buffer:
                            buffer.append(current_sub_set)
                            # print(f'Buffer atual: {buffer}')
            for i in buffer:
                response.append(list(i))
            current_max_size += 1
        return response
print(Solution().subsets(nums = [1,2,3]))