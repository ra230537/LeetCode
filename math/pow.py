class Solution:
    '''
    é basicamente uma função recursiva

    '''
    def pow(self, x, n) -> float:
        if (n == 0):
            return 1
        odd = n % 2 == 1
        n = n // 2
        response = self.pow(x * x, n)
        if odd:
            response = response * x
        return response
    def myPow(self, x: float, n: int) -> float:
        '''
        Da pra fazer em o(log(n))
        r = x

        x 5
                                        
        '''
        if (n == 0):
            return 1
        elif (n > 0):
            return self.pow(x, n)
        else:
            return self.pow(1/x, abs(n))
      
print(Solution().myPow(2, 2))