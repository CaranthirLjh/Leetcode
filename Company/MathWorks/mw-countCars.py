# https://www.1point3acres.com/bbs/thread-918621-1-1.html

class Solution:
    def countCars(self, numCars, hourStart):
        l = len(numCars)
        maxFrequence = [1]*l
        curMax = float("-inf")
        for i in range(l-1,-1,-1):
            cars = numCars[i]
            if cars <= curMax:
                maxFrequence[i] = maxFrequence[i+1]+1
            else:
                curMax = max(curMax,cars)
        ans = []
        for i in hourStart:
            ans.append(maxFrequence[i-1])
        return ans

if __name__ == "__main__":
    numCars = [5,4,5,3,2]
    hourStart = [1,2,4,5]
    ans = Solution().countCars(numCars,hourStart)
    assert(ans, [2,1,1,1])