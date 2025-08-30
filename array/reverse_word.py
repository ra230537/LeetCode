from collections import deque
class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        Eu preciso de um ponteiro para o inicio e um para o final
        Eu preciso de uma variavel para guardar a palavra de inicio e a palavra de final
        '''
        reversed_string = ''
        current_word = deque()
        for idx in range(len(s)-1, -1, -1):
            if (s[idx] == ' '):
                if (len(current_word) == 0):
                    continue
                else:
                    if (reversed_string != ''):
                        reversed_string += ' '
                    reversed_string += ''.join(current_word)
                    current_word = deque()
            else:
                current_word.appendleft(s[idx])
        if (len(current_word) > 0):
            if (reversed_string != ''):
                reversed_string += ' '
            reversed_string += ''.join(current_word)
        return reversed_string
print(list(Solution().reverseWords(s = "a good   example")))