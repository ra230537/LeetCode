from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Tu vai ter um k que representa o proximo numero diferente deveria estar
        Tu vai ter um contador porque agora a gente só vai atualizar k quando o contador for maior que 1
        '''
        k  = 1
        equal_count = 0
        for idx in range(len(nums)-1):
            if (nums[idx] == nums[idx+1]):
                equal_count +=1
                if (equal_count < 2):
                    k+=1
            else:
                print(f'Posicao k: {k+1};Posicao idx+1: {idx+2}; Valor idx+1: {nums[idx+1]}')
                nums[k] = nums[idx+1]
                k+=1
                equal_count = 0

        print(nums[:k])
        return k
print(Solution().removeDuplicates(nums = [0,0,1,1,1,1,2,3,3]))