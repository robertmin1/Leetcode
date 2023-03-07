# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def need(root):
            if not root:
                return 0
            return 1 + max(need(root.left), need(root.right))
        
        return  max(need(root.left) + need(root.right), max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)))