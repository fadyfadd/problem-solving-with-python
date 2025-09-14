class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def merge_two_lists(list1, list2):
            head=ListNode()
            last=head

            list1_pointer=list1
            list2_pointer=list2
            
            while (list1_pointer != None and list2_pointer != None):
                if (list1_pointer.val < list2_pointer.val):
                    last.next=list1_pointer
                    last=list1_pointer
                    list1_pointer = list1_pointer.next
                else:
                    last.next=list2_pointer
                    last=list2_pointer
                    list2_pointer = list2_pointer.next

            while (list1_pointer != None):
                    last.next=list1_pointer
                    last=list1_pointer
                    list1_pointer = list1_pointer.next

            while (list2_pointer != None):
                    last.next=list2_pointer
                    last=list2_pointer
                    list2_pointer = list2_pointer.next

            return head.next



a = ListNode(1, ListNode(3, ListNode(5)))
b = ListNode(2, ListNode(4, ListNode(6)))
merged = merge_two_lists(a, b)
while merged:
     print(merged.val, end=" -> ")
     merged = merged.next