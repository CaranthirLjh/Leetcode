# 99. Recover Binary Search Tree

# You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cache = list()
        vals = list()
        node = root
        small,large = None,None
        while(node or cache):
            while(node):
                cache.append(node)
                node = node.left
            if cache:
                node = cache.pop()
                if vals and node.val < vals[-1].val:
                    small = node
                    if not large:
                        large = vals[-1]
                    else:
                        break
                vals.append(node)
                node = node.right
        small.val,large.val = large.val,small.val