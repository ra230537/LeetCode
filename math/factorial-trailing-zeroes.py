class Solution:
    def trailingZeroes(self, n: int) -> int:
        '''
        A gente precisa formar 10
        Basta fatorar para descobrir quantos 5 há na fatoração
        e quantos 2 há na fatoração
        O resultado será o minimo entre os dois

        Uma forma mais fácil seria ver apenas o numero 5, porque o 5 sempre vai ser a borda inferior, então basta iterar por n e dividi-lo por 5
        '''
        count_2 = 0
        count_5 = 0
        for current_number in range(n, 0, -1):
            # print(f'Current number: {current_number}')
            while current_number % 2 == 0:
                current_number = current_number // 2
                count_2 += 1
            while current_number % 5 == 0:
                current_number = current_number // 5
                count_5 += 1
            # print(f'ha {count_2} numeros 2')
            # print(f'ha {count_5} numeros 5')
        return min(count_2, count_5)
        

print(Solution().trailingZeroes(n = 5))

assert Solution().trailingZeroes(n = 3) == 0
assert Solution().trailingZeroes(n = 5) == 1
assert Solution().trailingZeroes(n = 0) == 0