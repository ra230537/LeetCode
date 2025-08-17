# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from linked_list_utils import ListNode, create_linked_list, print_linked_list_as_array
class Solution:
    def deleteNode(self, node: Optional[ListNode]) -> Optional[ListNode]:
        p = node
        while p.next != None:
            # substitui o valor atual pelo proximo
            p.val = p.next.val
            #se o valor depois do proximo for none, estamos no penultimo, então o proximo já vira none
            if (p.next.next == None):
                p.next = None
                break
            # atualiza o ponteiro para a proxima casa
            p = p.next
head = create_linked_list([1])
response = Solution().isPalindrome(head)
print_linked_list_as_array(response)