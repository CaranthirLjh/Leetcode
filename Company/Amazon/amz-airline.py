# https://www.1point3acres.com/bbs/thread-922190-1-1.html

class Solution:
    def airline(self, forwardRouteList, returnRouteList, maxTravelList):
        L = len(returnRouteList)
        forwardRouteList.sort(key=lambda x:x[1])
        returnRouteList.sort(key=lambda x:x[1])

        def _binSearch(target):
            l,r = 0,L-1
            while(l<r):
                mid = (l+r+1)//2
                if returnRouteList[mid][1] == target:
                    return mid
                elif returnRouteList[mid][1] < target:
                    l = mid
                else:
                    r = mid-1
            return l
        
        cur = 0
        ans = []
        for i in range(len(forwardRouteList)):
            forward = forwardRouteList[i][1]
            j = _binSearch(maxTravelList-forward)
            back =  returnRouteList[j][1]
            if forward+back > maxTravelList:
                continue
            if forward+back == cur:
                ans.append([forwardRouteList[i][0],returnRouteList[j][0]])
            elif forward+back > cur:
                ans = [[forwardRouteList[i][0],returnRouteList[j][0]]]
                cur = forward+back
            else:
                continue
        return ans

if __name__ == "__main__":
    forwardRouteList = [[1,3000],[2,5000],[4,10000],[3,7000]]
    returnRouteList = [[1,2000],[2,3000],[3,4000],[4,5000]]
    maxTravelList = 10000
    ans = Solution().airline(forwardRouteList,returnRouteList,maxTravelList)
    print(ans)
    assert(ans, [[2,4],[3,2]])
    # forwardRouteList = [[1,2000],[2,4000],[3,6000]]
    # returnRouteList = [[1,2000]]
    # maxTravelList = 7000
    # ans = Solution().airline(forwardRouteList,returnRouteList,maxTravelList)
    # print(ans)
    # assert(ans, [[2,1]])