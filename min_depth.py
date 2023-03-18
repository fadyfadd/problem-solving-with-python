class TreeNode: 
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_depth(root: TreeNode): 
        
        if (root==None):
            return 0

        left_depth=min_depth(root.left)
        right_depth=min_depth(root.right)      

        if (left_depth==0 or right_depth==0):
            return max(left_depth , right_depth) + 1
        else:
            return min(left_depth ,right_depth) + 1     
