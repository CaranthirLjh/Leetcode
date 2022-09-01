# https://www.1point3acres.com/bbs/thread-921833-1-1.html

# 路灯题, 路灯是个范围. [[1,5], [2, 7],‍‌‌‌‍‌‍‌‍‌‌‍‌‍‍‌‌‍‍‌ points = [1, 4, 6], return [1, 2, 1] 要求return point被路灯照到的个数.

import bisect


class Solution:
    def coverByNLight(self, lights, points):
        starts = []
        ends = []
        l = len(lights)
        for s,e in lights:
            starts.append(s)
            ends.append(e)
        
        starts.sort()
        ends.sort()

        ans = []
        for p in points:
            before_start = l-bisect.bisect_right(starts,p)
            after_end = bisect.bisect_left(ends,p)
            ans.append(l-before_start-after_end)
        return ans

if __name__ == "__main__":
    lights = [[1,5], [2, 7], [3, 4]] 
    points = [1, 4, 6]
    ans = Solution().coverByNLight(lights, points)
    print(ans)
