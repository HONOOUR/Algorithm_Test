# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    arr: list = []
    def inorder(self, node):
        self.inorder(node.left)
        arr.insert(node.val)
        self.inorder(node.right)

    def inorderTraversal(self, tree_node):
        self.inorder(tree_node)


item = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
sol = Solution()
sol.inorderTraversal(item)
# root -> left -> root -> right
