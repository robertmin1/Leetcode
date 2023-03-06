# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        
    
        def checker(leftroot, rightroot):
            if leftroot == None and rightroot == None:
                return True
            elif leftroot != None and rightroot != None:
                return leftroot.val == rightroot.val and checker(leftroot.left,rightroot.right) and checker(leftroot.right, rightroot.left)
        
            return False
        
        return checker(root.left, root.right)
        
        