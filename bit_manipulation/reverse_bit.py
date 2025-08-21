class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        Preciso achar a posição do primeiro bit: i -> n - i, delta de n-2*i

        Achar a posição do primeiro bit menos signficativ: n & -n, se for 0 para
        Multiplicar response por n << 2 (n-2*i) vezes
        Remover esse bit n & (n-1)
        '''

        response = 0
        size_n = 32
        while n != 0:
            # Acha o valor do bit menos significativo
            i = n & (-n)
            count = 0
            # Acha a posição do bit menos significativo
            while i!=1:
                count+=1
                i = i >> 1
            # Soma na resposta final
            response += 1 << (size_n-count-1)

            # Remove o bit menos significativo
            n = n & (n-1)
        return response
    
print(Solution().reverseBits(43261596))


