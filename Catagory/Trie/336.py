# 336. Palindrome Pairs

# Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

from typing import List

class Trie:
    def __init__(self, val=""):
        self.val = val
        self.children = [None]*26
        self.ind = None
    
class Solution:
    def ispalindrome(self, s):
        return s == s[::-1]
        
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        root = Trie()
        
        for i,word in enumerate(words):
            node = root
            for c in word[::-1]:
                if not node.children[ord(c)-97]:
                    node.children[ord(c)-97] = Trie(val=c)
                node = node.children[ord(c)-97]
            node.ind = i
        
        ans = []
        
        def _dfs(node, cur):
            for c in node.children:
                if not c:
                    continue
                if c.ind is not None and self.ispalindrome(cur+c.val):
                    cands.append(c.ind)
                if c:
                    _dfs(c,cur+c.val)
        cands = []
        for i,word in enumerate(words):
            node = root
            offset = 0
            for c in word:
                if not node:
                    break
                if node.ind is not None and node.ind != i  and self.ispalindrome(word[offset:]):
                    ans.append([i,node.ind])
                node = node.children[ord(c)-97]
                offset += 1
            if node and node.ind is not None and node.ind != i  and self.ispalindrome(word[offset:]):
                ans.append([i,node.ind])
            if node:
                cands = []
                _dfs(node,"")
                for cand in cands:
                    ans.append([i,cand])
            
        return ans
            
if __name__ == "__main__":
    words = ["abcd","dcba","lls","s","sssll"]
    ans = Solution().palindromePairs(words)
    assert(ans, [[0,1],[1,0],[3,2],[2,4]])