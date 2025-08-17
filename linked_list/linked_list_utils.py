class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def create_linked_list(array: list[int]):
    if (len(array) == 0):
        return None
    head = ListNode()
    previous_node = head
    for idx in range(len(array)):
        current_node = ListNode(array[idx])
        previous_node.next = current_node
        previous_node = current_node
    return head.next
def print_linked_list_as_array(head: ListNode):
    result = []
    current_node = head
    while current_node != None:
        result.append(current_node.val)
        current_node = current_node.next
    print(result)
