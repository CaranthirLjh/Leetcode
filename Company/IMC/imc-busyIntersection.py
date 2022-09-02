# https://www.1point3acres.com/bbs/thread-917754-1-1.html

from collections import deque


class Solution:
    def busyIntersection(self, arrival, street):
        firstAve = deque([])
        mainSt =  deque([])
        
        l = len(arrival)
        for i in range(l):
            if street[i] == 0:
                mainSt.append((arrival[i],i))
            else:
                firstAve.append((arrival[i],i))
        
        time = 0
        ans = [-1]*l
        stPass = False

        while(firstAve or mainSt):
            if not firstAve:
                while(mainSt):
                    t,i = mainSt.popleft()
                    if t<=time:
                        ans[i] = time
                        time += 1
                    else:
                        ans[i] = t
                        time = t+1
            elif not mainSt:
                while(firstAve):
                    t,i = firstAve.popleft()
                    if t<=time:
                        ans[i] = time
                        time += 1
                    else:
                        ans[i] = t
                        time = t+1
            else:
                if mainSt[0][0] <= time and firstAve[0][0] <= time:
                    if stPass:
                        _,i = mainSt.popleft()
                    else:
                        _,i = firstAve.popleft()
                    ans[i] = time
                    time += 1
                elif mainSt[0][0] <= time:
                    _,i = mainSt.popleft()
                    ans[i] = time
                    time += 1
                    stPass = True
                elif firstAve[0][0] <= time:
                    _,i = firstAve.popleft()
                    ans[i] = time
                    time += 1
                    stPass = False
                else:
                    stPass = False
                    time = min(mainSt[0][0],firstAve[0][0])
        return ans

if __name__ == "__main__":
    arrival = [0,0,1,4]
    street = [0,1,1,0]
    ans = Solution().busyIntersection(arrival, street)
    print(ans)
