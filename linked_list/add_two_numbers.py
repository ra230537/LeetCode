# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from linked_list_utils import ListNode, create_linked_list, print_linked_list_as_array
class Solution:
    def revert_linked_list(self, head: ListNode):
        previous_node = None
        current_node: ListNode = head
        while True:
            next_node = current_node.next
            current_node.next = previous_node
            if next_node == None:
                break
            previous_node = current_node
            current_node = next_node
        return current_node
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Para cada numero, aponta para trás
        '''
        l1 = self.revert_linked_list(l1)
        l2 = self.revert_linked_list(l2)
        carry = 0
        head = ListNode()
        previous_node = head
        while l1 != None or l2 != None or carry > 0:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0
                
            result = (carry + first + second)
            carry = result // 10
            value = result % 10

            current = ListNode(value)
            previous_node.next = current
            previous_node = current

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next

l1 = create_linked_list([2, 4,3])
l2 = create_linked_list([5, 6,])
head = Solution().addTwoNumbers(l1, l2)
print_linked_list_as_array(head)