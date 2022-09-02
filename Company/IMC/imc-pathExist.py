# https://www.1point3acres.com/bbs/thread-917754-1-1.html

from math import sqrt


class Solution:
    def pathExist(self, c, x1, y1, x2, y2):
        if int(sqrt(x2+y2))**2 == x2+y2:
            return False
        
        row = abs(x2-x1)
        col = abs(y2-y1)

        dp = [[0]*(col+1) for _ in range(row+1)]
        dp[0][0] = 1

        for i in range(row+1):
            for j in range(col+1):
                if i == 0 and j == 0:
                    continue
                if int(sqrt(i+j+x1+y1))**2 == i+j+x1+y1:
                    continue
                if i>=j:
                    dp[i][j] += dp[i-j][j]
                else:
                    dp[i][j] += dp[i][j-1]
                if i>=c and j>=c:
                    dp[i][j] += dp[i-c][j-c]
        return dp[-1][-1] > 0

if __name__ == "__main__":
    c = 1
    x1,y1 = 1,4
    x2,y2 = 7,6
    ans = Solution().pathExist(c,x1,y1,x2,y2)
    print(ans)
