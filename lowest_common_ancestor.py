
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lowest_common_ancestor(root:TreeNode, p:TreeNode, q:TreeNode):

    if root is None:
        return None

    if root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right


# Sample binary tree:
#         3
#        / \
#       5   1
#      / \ / \
#     6  2 0  8
#       / \
#      7   4

# Create nodes
root = TreeNode(3)
node5 = TreeNode(5)
node1 = TreeNode(1)
node6 = TreeNode(6)
node2 = TreeNode(2)
node0 = TreeNode(0)
node8 = TreeNode(8)
node7 = TreeNode(7)
node4 = TreeNode(4)

# Build the tree
root.left = node5
root.right = node1
node5.left = node6
node5.right = node2
node1.left = node0
node1.right = node8
node2.left = node7
node2.right = node4

# Define p and q
p = node5  # Node with value 5
q = node1  # Node with value 1

# Call the function
ancestor = lowest_common_ancestor(root, p, q)
print(f"Lowest Common Ancestor of {p.val} and {q.val} is: {ancestor.val}")

