from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificReachable = deque([])
        atlanticReachable = deque([])
        
        row,col = len(heights),len(heights[0])
        
        for i in range(row):
            pacificReachable.append((i,0))
            atlanticReachable.append((i,col-1))
        for j in range(1,col):
            pacificReachable.append((0,j))
            atlanticReachable.append((row-1,col-j-1))
        
        moves = [-1,0,1,0,-1]
        
        def _bfs(cache):
            ans = set()
            seen = set(cache)
            while(cache):
                x,y = cache.popleft()
                ans.add((x,y))
                for i in range(4):
                    dx,dy = moves[i],moves[i+1]
                    if 0<=x+dx<row and 0<=y+dy<col and (x+dx,y+dy) not in seen:
                        if heights[x+dx][y+dy]<heights[x][y]:
                            continue
                        cache.append((x+dx,y+dy))
                        seen.add((x+dx,y+dy))
            return ans
        
        pacificReachable = _bfs(pacificReachable)
        atlanticReachable = _bfs(atlanticReachable)
        return list(pacificReachable & atlanticReachable)

if __name__ == "__main__":
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    ans = Solution().pacificAtlantic(heights)
    print(ans)
    assert ans == [(4, 0), (0, 4), (3, 1), (1, 4), (3, 0), (2, 2), (1, 3)]