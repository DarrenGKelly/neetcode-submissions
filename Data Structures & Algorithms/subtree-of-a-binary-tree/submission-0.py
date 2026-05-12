# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isEqual(root1, root2) -> bool:
            if (root1 is None or root2 is None):
                return root1 is None and root2 is None
            else:
                return root1.val == root2.val and isEqual(root1.left, root2.left) and isEqual(root1.right, root2.right)

        if (root is None):
            return False
            
        return isEqual(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)