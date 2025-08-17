# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional
from linked_list_utils import ListNode, create_linked_list, print_linked_list_as_array
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        Forma burra de se pensar:
        Vamos partir da cabeça, passar por cada item, marcar ele como 999999, se encontrarmos um numero 999999 fomos nos que marcamos então é ciclico
        '''
        work_pointer = head
        while (work_pointer != None):
            if (work_pointer.val == 999999):
                return True
            else:
                work_pointer.val = 999999
            work_pointer = work_pointer.next
        return False
head = create_linked_list([3,2,0,-4])
response = Solution().hasCycle(head)
print(response)