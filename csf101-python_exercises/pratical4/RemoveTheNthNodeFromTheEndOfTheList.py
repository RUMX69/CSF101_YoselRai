class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def display(head):
    elements = []
    current = head
    while current:
        elements.append(current.val)
        current = current.next
    print(f"[{', '.join(map(str, elements))}]")

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy
    
    # Move fast pointer n nodes ahead
    for _ in range(n):
        fast = fast.next
    
    # Move both pointers until fast reaches the end
    while fast.next:
        fast = fast.next
        slow = slow.next
    
    # Remove the nth node
    slow.next = slow.next.next
    
    return dummy.next


head = build_linked_list([1, 2, 3, 4, 5])
n = 2
new_head = removeNthFromEnd(head, n)
display(new_head)