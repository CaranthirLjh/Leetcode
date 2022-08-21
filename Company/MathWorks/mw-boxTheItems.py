class Solution:
    def boxTheItems(self, total: int, k: int) -> int:
        dp = [0]*(total+1)
        dp[0] = 1
        
        for w in range(1,k+1):
            for i in range(w,total+1):
                dp[i] += dp[i-w]
        return dp[-1]
    
if __name__ == "__main__":
    total = 7
    k = 2
    ans = Solution().boxTheItems(total,k)
    assert(ans, 4)