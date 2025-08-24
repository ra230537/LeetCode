from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        Precisamos fazer em log(n) o seguinte:
        Achar um elemento cujo os dois vizinhos são menores que ele

        Faz uma busca binária mas o motivador da busca binaria vai ser o lado que tem um elemento maior
        Em algum momento voce vai encontrar um topo
        '''
        size = len(nums)
        floor = 0
        ceil = size - 1
        mid = (floor + ceil) // 2
        while floor <= ceil:
            if ((mid == size-1 or nums[mid + 1] < nums[mid]) and (mid == 0 or nums[mid - 1] < nums[mid]) ):
                return mid
            elif(nums[mid + 1] > nums[mid]):
                floor = mid + 1
            elif(nums[mid - 1] > nums[mid]):
                ceil = mid - 1
            mid = (floor + ceil) // 2
        return mid
print(Solution().findPeakElement([1,2,1,3,5,6,4]))