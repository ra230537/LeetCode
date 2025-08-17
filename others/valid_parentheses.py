class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Para fazer essa vamos precisar de uma pilha
        Podemos chamar parenteses abrindo de 1
        colchetes de 2
        chaves de 3
        e suas versões fechadas ficam sendo -1, -2, e -3
        A ideia é ir empilhando, valores positivos são permitidos sempre a ser empilhados, mas para desempilhar o valor tem que somar 0
        com o topo da pilha
        '''
        stack = []
        size = 0
        for idx, value in enumerate(s):
            control = 0
            match value:
                case '(':
                    control = 1
                case '[':
                    control = 2
                case '{':
                    control = 3
                case ')':
                    control = -1
                case ']':
                    control = -2
                case '}':
                    control = -3
            if (control > 0):
                stack.append(control)
                size+=1
            elif(control < 0):
                if(size == 0):
                    return False
                if (stack[-1] + control != 0):
                    return False
                else:
                    stack.pop()
                    size-=1
        if (size == 0):
            return True
        else:
            return False
print(Solution().isValid(s = "([)]"))
