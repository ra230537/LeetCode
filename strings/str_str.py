
'''
O algoritmo usado é o KMP
O kmp ele se aproveita de uma invariante que guarda o maior prefixo que também é sufixo de todos os prefixos proprios do padrão (needle)
Dai o pulo do gato é: quando acontece um miss match, a gente pode voltar para a ultima posição do ultimo maior prefixo que também é sufixo
se aproveitando do seguinte:
Tu sabe que até a posição j-1 encaixa até i-1.
Tu sabe também que o fim desse cara j-1 é encaixado com o a posição [0..lps[j-1]] já que é prefixo que é sufixo
Então, esse [0..lps[j-1]] também vai encaixar com até a ultima posição i-1, basta então comparar lps[j-1] com i
'''
class Solution:
    def get_lps(self, pattern: str) -> list[int]:
        n = len(pattern)
        lps = [0] * n
        j = 0
        i = 1
        while i < n:
            if (pattern[i] == pattern[j]):
                j += 1
                lps[i] = j
                i += 1
            else:
                if (j != 0):
                    j = lps[j-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        j = 0
        n = len(haystack)
        i = 0
        lps = self.get_lps(needle)
        while i < n:
            if (needle[j] == haystack[i]):
                i += 1
                j += 1
            if (j == m):
                return i - j
            elif (i < n and needle[j] != haystack[i]):
                if (j != 0):
                    j = lps[j-1]
                else:
                    i+=1
        return -1
print(Solution().strStr(haystack = "leetcode", needle = "leeto"))