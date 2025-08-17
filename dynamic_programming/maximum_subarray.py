class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ''' Algoritmo:
        vamos ter um ponteiro para indicar o começo e o fim do subarray maximo
        e outro para indicar o começo e o fim do atual
        uma variavel para controle de soma
        Caso a soma fique negativa, o subarray atual é descartado => ponteiros de inicio e fim começam no proximo
        Caso a soma atual fique maior que a soma maxima -> atualiza os indicadores de começo e fim
        '''

        current_sum = 0
        response_sum = 0
        for i in range(len(nums)):
            current_sum+=nums[i]
            if (current_sum < 0):
                current_sum = 0
            if (current_sum >= response_sum):
                response_sum = current_sum
        max_value = max(nums)
        if (max_value < 0):
            response_sum = max_value
        return response_sum
print(Solution().maxSubArray(nums = [-1]))

'''
Usando divisão e conquista: função que acha o maior valor:
cahmar ela pra metade da esquerda, metade da direita
para o meio (começa esquerda e termina direita) fazer uma soma a esquerda atualizando uma variavel de controle + sfazer soma da direita
atualizando a variavel de controle

'''