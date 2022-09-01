# https://www.1point3acres.com/bbs/thread-920186-1-1.html

class Solution:
    def bubbleDelete(self,matrix):
        row,col = len(matrix),len(matrix[0])
        tobeDelete = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    continue
                cur = matrix[i][j]
                cache = [(i,j)]
                
                if i<=row-3:
                    _cache = []
                    for k in range(i+1,row):
                        if matrix[k][j] != cur:
                            break
                        _cache.append((k,j))
                    if len(_cache)>=2:
                        cache.extend(_cache)
                if j<=col-3:
                    _cache = []
                    for k in range(j+1,col):
                        if matrix[i][k] != cur:
                            break
                        _cache.append((i,k))
                    if len(_cache)>=2:
                        cache.extend(_cache)
                if len(cache)>1:
                    tobeDelete |= set(cache)
        
        for x,y in tobeDelete:
            matrix[x][y] = 0

        for j in range(col):
            cur = row-1
            for i in range(row-1,-1,-1):
                if matrix[i][j] == 0:
                    continue
                matrix[cur][j] = matrix[i][j]
                cur -= 1
            for k in range(cur,-1,-1):
                matrix[k][j] = 0
        return matrix

if __name__ == "__main__":
    matrix = [
        [1,2,3,4,5],
        [1,1,1,4,4],
        [1,2,3,4,5],
        [2,4,5,1,2],
    ]
    ans = Solution().bubbleDelete(matrix)
    print(ans)
