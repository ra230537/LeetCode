'''
TODO: Anotar que uma lista é uma pilha no python.
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        .. -> desempilha
        . -> não faz nada
        / -> split
        
        '''
        path = path.split('/')
        stack = []
        for element in path:
            if element == '..':
                if(stack != []):
                    stack.pop()
                else:
                    continue
            elif element == '.' or element == '':
                continue
            else:
                stack.append(element)


        return '/' + '/'.join(stack)
print(Solution().simplifyPath(path = "/.../a/../b/c/../d/./"))