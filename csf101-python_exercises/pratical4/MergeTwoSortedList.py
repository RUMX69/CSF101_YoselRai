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

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    if list1:
        current.next = list1
    if list2:
        current.next = list2
    
    return dummy.next

def display(head):
    elements = []
    current = head
    while current:
        elements.append(current.val)
        current = current.next
    print(f"[{', '.join(map(str, elements))}]")

# Build linked lists from Python lists
list1 = build_linked_list([1,2,4])
list2 = build_linked_list([1,3,4])

# Merge and display
merged = mergeTwoLists(list1, list2)
display(merged)