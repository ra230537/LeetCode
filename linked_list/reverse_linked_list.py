# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from linked_list_utils import ListNode, create_linked_list, print_linked_list_as_array
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Iterativamente:
        Cria o dummy
        aponta o dummy para o previous
        '''
        if (head == None):
            return None
        previous_node = ListNode(head.val)
        current_node = head.next
        while current_node != None:
            # cria o novo nó
            new_node = ListNode(current_node.val)
            # diz que o próximo nó desse cara, é o anterior
            new_node.next = previous_node
            print(f'{previous_node.val} <- {new_node.val}')
            # atualiza nosso nó de trabalho, coloca ele pra frente
            previous_node = new_node
            # Atualiza o nosso nó de iteração
            current_node = current_node.next
        return previous_node

head = create_linked_list([1, 2])
reversed_head = Solution().reverseList(head)
print_linked_list_as_array(reversed_head)