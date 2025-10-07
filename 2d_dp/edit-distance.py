from collections import deque
class Solution:


    def minDistance(self, word1: str, word2: str) -> int:
        '''
        Para cada letra da palavra 1
        Eu alinho a palavra 2, as letras da palavra 1 que não houverem na palavra 2 são adições e o contrário 
        Palavra 1 and not palavra 2:
            remoção
        Not palavra 1 and palavra 2
            adição
        Palavra 1 and palavra 2
            substituição
        '''
        if word2 == "":
            return len(word1)
        if word1 == "":
            return len(word2)
        dp = [[99999 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        # deleção e replace
        for j in range(len(dp[0])):
            dp[0][j] = j
        # Adição e replace
        for i in range(len(dp)):
            dp[i][0] = i
        # Deleção, adição e
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if (word1[i-1] == word2[j-1]):
                    dp[i][j] = dp[i-1][j-1]
                else:
                    addition = dp[i-1][j] # Adiciono uma letra para bater com i-1 e continuo com j
                    deletion = dp[i][j-1] # deletei a ultima letra e agora estou comparando i com j
                    replace = dp[i-1][j-1] # Dei replace na ultima letra de i - 1 e 
                    dp[i][j] = min(addition, deletion, replace)
                    dp[i][j] += 1
        return dp[-1][-1]
print(Solution().minDistance(word1 = "horse", word2 = "ros"))

'''
a
aa

sea
eat
'''