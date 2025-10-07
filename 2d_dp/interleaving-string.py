class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        Para cada letra de s3
        vamos ter uma linha em uma matriz
        essa cada elemento da linha vai ter dois valores: idx_1 e idx_2 que vai ser o proximo indice da respectiva palavra que formou a substring s3 até agora
        Para construir a proxima letra (adicionar uma linha na matriz)
        precisamos percorrer cada coluna da linha anterior e ver se a letra é igual a letra atual de s3, 
        se for adicionamos na nova linha

        No fim, se chegar num ponto que nada funciona, então a resposta final será false
        '''
        dp=[[]]
        if (s1 == "" and s2 == "" and s3 == ""):
            return True
        if (len(s3) != len(s1)+len(s2)):
            return False
        if len(s1) > 0 and s1[0] == s3[0]:
            dp[0].append((1, 0))
        if len(s2) > 0 and s2[0] == s3[0]:
            dp[0].append((0, 1))
        for idx_3 in range(1, len(s3)):
            current_list = []
            for idx_1, idx_2 in dp[-1]:
                if idx_1 < len(s1) and s1[idx_1] == s3[idx_3]:
                    if ((idx_1 + 1, idx_2) not in current_list):
                        current_list.append((idx_1 + 1, idx_2))
                if idx_2 < len(s2) and s2[idx_2] == s3[idx_3]:
                    if ((idx_1, idx_2 + 1) not in current_list):
                        current_list.append((idx_1, idx_2 + 1)) 
            dp.append(current_list)
        # print(dp)
        if dp[-1] != []:
            return True
        return False

        
print(Solution().isInterleave(s1 = "abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb", s2 = "ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc", s3 = "cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc"))