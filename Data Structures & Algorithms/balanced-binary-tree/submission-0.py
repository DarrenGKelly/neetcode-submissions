from math import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def getHeight(root: Optional[TreeNode]) -> int:
            if (root is None):
                return 0
            else:
                return max(getHeight(root.left), getHeight(root.right)) + 1
        
        if (root is None):
            return True
        else:
            return (self.isBalanced(root.right) and self.isBalanced(root.left) and (abs(getHeight(root.right) - getHeight(root.left)) <= 1))