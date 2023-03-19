def reverse_list(head):
       prev=None
       curr=head

       while (curr != None):
            temp_next = curr.next
            curr.next = prev            
            prev = curr
            curr = temp_next
       return prev;