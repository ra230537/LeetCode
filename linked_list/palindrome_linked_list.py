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
            # atualiza nosso nó de trabalho, coloca ele pra frente
            previous_node = new_node
            # Atualiza o nosso nó de iteração
            current_node = current_node.next
        return previous_node

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reversed_head = self.reverseList(head)
        while (head != None):
            if (reversed_head.val != head.val):
                return False
            reversed_head = reversed_head.next
            head = head.next
        return True
head = create_linked_list([1])
response = Solution().isPalindrome(head)
print(response)