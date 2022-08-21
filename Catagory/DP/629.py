# 629. K Inverse Pairs Array

# For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

# Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0]*(k+1) for _ in range(n+1)]
        prev = 0
        for i in range(1,n+1):
            for j in range(k+1):
                if i == 1 and j == 0:
                    dp[i][j] = 1
                    break
                elif j == 0:
                    dp[i][j] = 1
                else:
                    if j>=i:
                        dp[i][j] = dp[i][j-1]-dp[i-1][j-i]+dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-1]+dp[i-1][j]
        return dp[n][k]%(10**9+7)

if __name__ == "__main__":
    n=3
    k=1
    ans = Solution().kInversePairs(n,k)
    assert(ans,2)