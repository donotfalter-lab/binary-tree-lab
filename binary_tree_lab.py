from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

def max_depth(root: Optional[TreeNode]) -> int:
    # An empty tree has depth 0; otherwise count this node plus the deeper subtree
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Walk down the BST: if both values are on one side, go that way;
    # otherwise the current node is where the paths split (the LCA)
    node = root
    while node:
        if p.val < node.val and q.val < node.val:
            node = node.left
        elif p.val > node.val and q.val > node.val:
            node = node.right
        else:
            return node
    return node
