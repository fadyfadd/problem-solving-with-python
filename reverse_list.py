class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode) -> ListNode:
    prev = None
    curr = head

    while curr:
        temp_next = curr.next
        curr.next = prev
        prev = curr
        curr = temp_next

    return prev

 
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4)))) 
reversed_head = reverse_list(head) 
curr = reversed_head
while curr:
    print(curr.val, end=" -> " if curr.next else "\n")
    curr = curr.next

# 4 -> 3 -> 2 -> 1
