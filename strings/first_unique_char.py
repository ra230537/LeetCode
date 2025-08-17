class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        Achar o primeiro que não repete: O(n^2) -> Solução obvia
        Vou ter um vetor de 26 caracteres
        vou incrementar cada casa com a respectiva posição
        Vou passar denovo no vetor e verificar quantas ocorrencias acontecerem, se alguma for 1, retorno
        Se o vetor acabar, eu retorno -1.
        Uma otimização seria guardar a posição do vetor ao invés da quantidade e depois marcar com um valor dummy caso aparecesse novamente
        Dai seria so percorrer o vetor de memoria que tem tamanho constante
        '''
        memory = [0 for _ in range(26)]
        for letter in s:
            memory[ord(letter) - ord('a')]+=1
        for idx, letter in enumerate(s):
            if (memory[ord(letter) - ord('a')] == 1):
                return idx
        return -1
