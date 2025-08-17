from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        response = ["" for _ in range(n)]
        for i in range(1, n + 1):
            if i%3 == 0:
                response[i-1]+="Fizz"
            if i%5 == 0:
                response[i-1]+="Buzz"
            if i%5 !=0 and i%3 != 0:
                response[i-1] += str(i)
        return response