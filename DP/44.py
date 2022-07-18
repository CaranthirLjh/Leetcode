# 44. Wildcard Matching

# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls,lp = len(s),len(p)
        dp = [[False]*(lp+1) for _ in range(ls+1)]
        dp[0][0] = True
        for j in range(1,lp+1):
            if p[j-1]!="*":
                break
            dp[0][j] = True
        
        for i in range(1,ls+1):
            for j in range(1,lp+1):
                cs,cp = s[i-1],p[j-1]
                if cp in {cs,"?"}:
                    dp[i][j] = dp[i-1][j-1]
                elif cp == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1] or dp[i-1][j-1]
        return dp[-1][-1]

if __name__ == "__main__":
    s = "cb"
    p = "?a"
    ans = Solution().isMatch(s,p)
    assert(ans, False)