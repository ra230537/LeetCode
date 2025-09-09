from typing import Optional
from linked_list_utils import ListNode, create_linked_list, print_linked_list_as_array
'''
TODO: REVISAR PARA RELEMBRAR COMO CONSTROI UMA LISTA LIGADA
OLHAMOS PARA O DUMMY E PARA FRENTE O VALOR ATUAL VAI SER O PROXIMO VALOR A SE COLOCAR NA LISTA LIGADA
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Para cada numero, aponta para trás
        '''
        carry = 0
        head = ListNode()
        cursor = head
        while l1 != None or l2 != None or carry > 0:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0
                
            result = (carry + first + second)
            carry = result // 10
            value = result % 10

            cursor.next = ListNode(value)
            cursor = cursor.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next

l1 = create_linked_list([2, 4, 9])
l2 = create_linked_list([5, 6, 4, 9])
head = Solution().addTwoNumbers(l1, l2)
print_linked_list_as_array(head)