class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        '''
        Dado que eu sei qual a soma desses valores, basta que eu veja quanto da a soma e subtrair do valor teorico 
        teorico = n * (n + 1) / 2
        '''
        n = len(nums)
        theorical_sum = n * (n + 1) // 2
        practical_sum = sum(nums)
        return theorical_sum - practical_sum