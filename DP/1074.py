# 1074. Number of Submatrices That Sum to Target

# Given a matrix and a target, return the number of non-empty submatrices that sum to target.

# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

from typing import List
from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row,col = len(matrix),len(matrix[0])
        prefix = [[0]*(col+1) for _ in range(row+1)]
        
        for i in range(1,row+1):
            for j in range(1,col+1):
                prefix[i][j] = prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]+matrix[i-1][j-1]
        
        ans = 0
        for i in range(1,row+1):
            for j in range(i):
                count = defaultdict(int)
                for k in range(col+1):
                    cur = prefix[i][k]-prefix[j][k]
                    ans += count[cur-target]
                    count[cur]+=1
        return ans

if __name__ == "__main__":
    matrix = [[0,1,0],[1,1,1],[0,1,0]]
    target = 0
    ans = Solution().numSubmatrixSumTarget(matrix, target)
    assert(ans, 4)