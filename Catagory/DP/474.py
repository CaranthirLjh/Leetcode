from collections import Counter
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        for s in strs:
            counter = Counter(s)
            ones = counter["1"]
            zeros = counter["0"]
            for i in range(m,zeros-1,-1):
                for j in range(n,ones-1,-1):
                    dp[i][j] = max(dp[i][j],dp[i-zeros][j-ones]+1)
        return dp[-1][-1]

if __name__ == "__main__":
    strs = ["10","0001","111001","1","0"]
    m = 5
    n = 3
    ans = Solution().findMaxForm(strs, m, n)
    assert ans == 4