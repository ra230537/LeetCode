# Solução correta

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if (len(a) > len(b)):
            b = '0'*(len(a) - len(b))+b
        else:
            a = '0'*(len(b) - len(a))+a
        # Prevenir overflow
        a = '0'+a
        b = '0'+b
        response = ''
        carry = 0
        for idx in range(len(a)-1,-1,-1):
            a_int = int(a[idx])
            b_int = int(b[idx])
            result = a_int ^ b_int ^ carry
            response += str(result)
            carry = (a_int & b_int) | (a_int & carry) | (carry & b_int)
        response = response[::-1]
        if (response[0] == '0'):
            return response[1:]
        else:
            return response
print(Solution().addBinary(a = "1010", b = "1011"))

'''
Solução preguiçosa, porém rápida
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if (len(a) > len(b)):
            b = '0'*(len(a) - len(b))+b
            print(b)
        else:
            a = '0'*(len(b) - len(a))+a
        return str(bin(int(a, 2)+int(b, 2)))[2:]
'''
