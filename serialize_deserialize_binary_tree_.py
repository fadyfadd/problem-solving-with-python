from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

class SerializeDeserializeBinaryTree:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "/,"
        return f"{root.val},{self.serialize(root.left)}{self.serialize(root.right)}"

    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = deque(data.split(","))
        return self._deserialize_helper(nodes)

    def _deserialize_helper(self, nodes: deque) -> Optional[TreeNode]:
        val = nodes.popleft()
        if val == "/" or val == "":
            return None
        node = TreeNode(int(val))
        node.left = self._deserialize_helper(nodes)
        node.right = self._deserialize_helper(nodes)
        return node


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
ser = SerializeDeserializeBinaryTree()
data = ser.serialize(root)
print(data)
new_root = ser.deserialize(data)
print(new_root)
