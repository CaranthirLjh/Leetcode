# 72. Edit Distance

# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1,l2 = len(word1),len(word2)
        
        dp = [[0]*(l2+1) for _ in range(l1+1)]
        for i in range(1,l1+1):
            dp[i][0] = i
        for j in range(1,l2+1):
            dp[0][j] = j
        
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1])
                else:
                    dp[i][j] = 1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        return dp[-1][-1]

if __name__ == "__main__":
    word1 = "intention"
    word2 = "execution"
    ans = Solution().minDistance(word1,word2)
    assert(ans, 5)