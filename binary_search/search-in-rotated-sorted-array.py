from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        A gente tem um vetor, ele ta rotacionado e a gente precisa encontrar em log(n) se o valor está lá

        Possibilidade:
        Achar a posição do maior valor i
            Olho o ultimo
            Olho o do meio
            Se meio < ultimo:
                Pode ser ok, então o meio vira o ultimo e conitnua
            Se meio > ultimo:
                Tá errado, então eu sei que a rotação tá entre o meio e o ultimo. meio vira o inicio
        Fazer duas buscas binárias [0..i] e [i+1 .. n-1]
        '''
        floor = 0
        ceil = len(nums)-1
        mid = (floor + ceil)//2
        max_value = -9999999
        max_idx = -1
        while floor <= ceil:
            print(f'Piso:({floor}, {nums[floor]}); Meio:{(mid, nums[mid] )}; Ultimo: {(ceil, nums[ceil]) }')
            if (nums[ceil] < nums[mid]):
                if max_value < nums[mid]:
                    max_idx = mid
                    max_value = nums[mid]
                floor = mid + 1

            else:
                if max_value < nums[ceil]:
                    max_idx = ceil
                    max_value = nums[ceil]
                ceil = mid - 1
            mid = (floor + ceil)//2
        def binary_search(array, target):
            floor = 0
            ceil = len(array)-1
            mid = (floor + ceil)//2
            while floor <= ceil:
                if (array[mid] < target):
                    floor = mid + 1
                elif (array[mid] > target):
                    ceil = mid - 1
                else:
                    return mid
                mid = (floor + ceil)//2
            return -1
        # print(f'maximo idx: {max_idx}')
        # print(f'vetor 1: {nums[0:max_idx + 1]}')
        # print(f'vetor 2: {nums[max_idx + 1:len(nums)]}')
        r1 = binary_search(nums[0:max_idx + 1], target)
        r2 = binary_search(nums[max_idx + 1:len(nums)], target)
        if (r2 != -1):
            r2 += max_idx + 1
        return max(r1, r2)
print(Solution().search(nums = [7,8,9,0,1,2,3,4,5,6], target = 1))

assert Solution().search(nums = [4,5,6,7,0,1,2], target = 0) == 4
assert Solution().search(nums = [4,5,6,7,0,1,2], target = 3) == -1
assert Solution().search(nums = [1], target = 0) == -1


