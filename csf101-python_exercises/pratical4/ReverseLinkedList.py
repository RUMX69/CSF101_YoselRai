class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
    
    '''def reversedList(head):
        prev = None
        current = head
    
        while current:
            next_temp = current.next 
            current.next = prev
            prev = current
            current = next_temp
        return prev '''
    
    def append(self, value):
        new_node = ListNode(value)
        if not self.value:
            self.value = new_node
            return
        current = self.value
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.value
        while current:
            elements.append(current.value)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def reverse(self):
        prev = None
        current = self.value
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.value = prev

ll = ListNode()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.reverse()
ll.display()


