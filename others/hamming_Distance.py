class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # aqui só vão sobrar quem de fato é diferente
        xor_response = x ^ y
        count = 0
        # Forma de contar quantos bits tem
        # a forma de pensar é simples, basta pensar que quando voce subtrai 1
        # voce remove tanto o ultimo 1 do valor quanto todos os outros do valor subtraido de 1
        # então so vao sobrar os 1 a frente
        while (xor_response > 0):
            xor_response = xor_response & (xor_response - 1)
            count += 1
        return count