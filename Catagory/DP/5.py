# 5. Longest Palindromic Substring

# Given a string s, return the longest palindromic substring in s.

class Solution1:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        l = len(s)
        dp = [[False]*l for _ in range(l)]
        for i in range(l):
            dp[i][i] = True
        
        for i in range(2,l+1):
            for j in range(l-i+1):
                start,end = j,j+i-1
                if i == 2:
                    if s[start]==s[end]:
                        dp[start][end] = True
                        if end-start+1>len(ans):
                            ans = s[start:end+1]
                else:
                    if dp[start+1][end-1] and s[start]==s[end]:
                        dp[start][end] = True
                        if end-start+1>len(ans):
                            ans = s[start:end+1]
        
        return ans

class Solution2:
    def expand(self, head: int, end: int, s: str) -> int:
        l = len(s)
        while(head-1>=0 and end+1<l and s[head-1]==s[end+1]):
            head-=1
            end+=1
        return (head,end,end-head+1)
        
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        if l == 0:
            return ""
        
        ans = s[0]
        for i in range(l):
            s1,e1,l1 = self.expand(i, i, s)
            s2,e2,l2 = self.expand(i, i+1, s) if i+1<l and s[i]==s[i+1] else (0,0,0)
            if l2 > len(ans):
                ans = s[s2:e2+1]
            if l1 > len(ans):
                ans = s[s1:e1+1]
        return ans
                
        

if __name__ == "__main__":
    s = "cbbd"
    ans1 = Solution1().longestPalindrome(s)
    ans2 = Solution2().longestPalindrome(s)
    assert(ans1, "bb")
    assert(ans2, "bb")
