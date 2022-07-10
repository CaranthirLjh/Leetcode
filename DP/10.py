# 10. Regular Expression Matching

# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

from collections import defaultdict

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = defaultdict(bool)
        
        def _match(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            
            if j == len(p):
                ans = (i==len(s))
            else:
                first_match = i<len(s) and p[j] in {s[i],'.'}
                if j+1<len(p) and p[j+1] == "*":
                    ans = _match(i,j+2) or (first_match and _match(i+1,j))
                else:
                    ans = first_match and _match(i+1,j+1)
            dp[(i,j)] = ans
            return ans
        
        return _match(0,0)

if __name__ == "__main__":
    s = "ab"
    p = ".*"
    ans = Solution().isMatch(s, p)
    assert(ans, True)