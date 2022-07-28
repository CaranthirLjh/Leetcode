# 95. Unique Binary Search Trees II

# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def _genTree(left,right):
            if left>right:
                return [None,]
            if left == right:
                return [TreeNode(val=left)]
            
            allTrees = list()
            for i in range(left,right+1):
                leftTree = _genTree(left,i-1)
                rightTree = _genTree(i+1,right)
                
                for l in leftTree:
                    for r in rightTree:
                        node = TreeNode(val=i,left=l,right=r)
                        allTrees.append(node)
            return allTrees
        
        return _genTree(1,n)
                        
            