from typing import List, Dict


class Solution:
    dont_exist_list = []
    def is_suffix(self, s: str):
        for suffix in self.dont_exist_list:
            if s == suffix:
                return True
        return False
    def verify_word_in_dict(self, s: str, wordDict: Dict[str, bool]):
        if s == "":
            return True
        for i in range(1, len(s) + 1):
            print(f'Palavra atual {s[:i]}')
            if s[:i] in wordDict:
                print(f'1. {s[:i]} está no dicionario')
                if not self.is_suffix(s[i:]):
                    print(f'A palavra {s[i:]} tem um sufixo que não está proibido, vamos verificar...')
                    response = self.verify_word_in_dict(s[i:], wordDict)
                    if response:
                        print(f'2. {s[i:]} está no dicionário')
                        return response
                    else:
                        print(f'{s[i:]} não está no dicionário')
                else:
                    print(f'O sufixo {s[i:]} está proibido, passando para o proximo...')
        self.dont_exist_list.append(s)
        print(f"Lista não existentes: {self.dont_exist_list}")
        return False
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        luz, luzia, ial
        luzial
        Função vai para cada letra, verificar se a atual existe e se o outro segmento existe, para isso basta chamar recursivamente uma função para fazer isso
        """
        dictionary = dict(zip(wordDict, [True for _ in range(len(wordDict))]))
        return self.verify_word_in_dict(s, dictionary)

print(Solution().wordBreak(s = "catsandogcat", wordDict = ["cats","dog","sand","and","cat","an"]))

