# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        
        root = TreeNode(val=preorder[0])
        for ind,num in enumerate(inorder):
            if num == preorder[0]:
                break
        root.left = self.buildTree(preorder[1:ind+1],inorder[:ind])
        root.right = self.buildTree(preorder[ind+1:],inorder[ind+1:])
        return root
        