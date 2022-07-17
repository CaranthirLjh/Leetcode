# 32. Longest Valid Parentheses

# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        l = len(s)
        dp = [0]*l
        
        for i,c in enumerate(s):
            if c == ")":
                if i>=1 and s[i-1] == "(":
                    dp[i] = dp[i-2]+2 if i>=2 else 2
                elif i>=1 and s[i-1] == ")":
                    if i>=1 and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1] == "(":
                        dp[i] = dp[i-1]+2+dp[i-dp[i-1]-2] if i-dp[i-1]-2>=0 else dp[i-1]+2
        return max(dp)

if __name__ == "__main__":
    s = "()(())"
    ans = Solution().longestValidParentheses(s)
    assert(ans,s)