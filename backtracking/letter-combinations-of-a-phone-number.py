from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        Um problema de tamanho n
        é resolvido concatenando todas as possibilidades de [teclado_numerico[digits[n]]] 
        com todas as possibilidades do vetor de possibilidades
        P(n) = P(n-1) + n
        '''
        teclado_numerico = {
                '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'
            }
        if digits == "":
            return []
        combinations = [""]
        for digit in digits:
            possibilities_n = list(teclado_numerico[digit])
            new_combination = []
            for combination in combinations:
                for possibility in possibilities_n:
                    new_combination.append(combination + possibility)
            combinations = new_combination.copy()
        return combinations



assert Solution().letterCombinations(digits = "23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]

assert Solution().letterCombinations(digits = "") == []

assert Solution().letterCombinations(digits = "2") == ["a","b","c"]