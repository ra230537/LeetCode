class Solution:
    '''
    Ele fala na questão que repete em ciclo, então entendemos que se acontecer um resultado novamente é porque deu errado
    '''
    def isHappy(self, n: int) -> bool:
        results = {}
        while n != 1:
            temp = n
            result = 0
            while temp != 0:
                # Obtem o ultimo valor
                result += (temp % 10) ** 2
                # Remove o ultimo valor
                temp = temp // 10
            if result in results:
                return False
            # Cria um dicionario dummy apenas para se aproveitar da menor complexidade do dicionario em relação ao set
            results[result] = 0
            n = result
        return True
print(Solution().isHappy(19))