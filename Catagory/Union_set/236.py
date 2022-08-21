# 236. Lowest Common Ancestor of a Binary Tree

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        seen = set()
        anc = {}
        
        def _find(node):
            if anc[node] == node:
                return node
            return _find(anc[node])
        
        def _union(parent, child):
            pAnc = _find(parent)
            cAnc = _find(child)
            anc[cAnc] = pAnc
        
        ans = None
        def _dfs(node,prev):
            nonlocal ans
            if ans:
                return
            if not node:
                return
            
            if node == p:
                if q.val in seen:
                    ans = _find(q)
            elif node == q:
                if p.val in seen:
                    ans = _find(p)
            seen.add(node.val)
            anc[node] = node
            _dfs(node.left, node)
            _dfs(node.right, node)
            if prev:
                _union(prev, node)
        
        _dfs(root, None)
        return ans