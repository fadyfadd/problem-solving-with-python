class TreeNode: 
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def reverse_list(head:TreeNode):
       prev=None
       curr=head

       while (curr != None):
            temp_next = curr.next
            curr.next = prev            
            prev = curr
            curr = temp_next
       return prev