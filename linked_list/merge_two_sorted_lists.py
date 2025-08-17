# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from linked_list_utils import ListNode, create_linked_list, print_linked_list_as_array
class Solution:


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 == None and list2 == None):
            return None
        elif (list1 == None):
            return list2
        elif (list2 == None):
            return list1
        p1 = list1
        p2 = list2
        if (p1.val <= p2.val):
            head = list1
            p1 = p1.next
        else:
            head = list2
            p2 = p2.next
        tail = head
        while (p1 != None and p2 != None):
            if (p1.val <= p2.val):
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next
        if(p1 != None):
            tail.next = p1
        elif (p2 != None):
            tail.next = p2
        return head
head_1 = create_linked_list([3, 5])
head_2 = create_linked_list([1, 2, 4])
response = Solution().mergeTwoLists(head_2, head_1)
print_linked_list_as_array(response)
'''
No final sabemos que o seguinte:
quando temos p1, ele aponta para o endereço de memoria do começo de list
quando atribuidos algo a p1.next, estamos dizendo que o proximo objeto vai ter certo valor
quando atribuimos algo a p1, estamos falando que essa variavel p1, agora aponta para um novo endereço
no final, p1 eh apenas um apontador de endereços, podemos mudar ele tranquilamente o importante eh que list1 continua intacto e alteramos os proximos endereços

'''