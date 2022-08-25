# https://leetcode.com/discuss/interview-experience/1316685/Amazon-OA-SDE1-(new-questions)

# You are given a List of Integers which is a list of priorities. A priority can be a number from 1-99. 
# Without changing the order of the array, minimize the priority as much as possible without changing the order.


import heapq


class Solution:
    def minPriority(self, arr):
        minHeap = [(v,i) for i,v in enumerate(arr)]
        heapq.heapify(minHeap)
        priority = 0
        ans = [0]*len(arr)
        prev = None
        while(minHeap):
            v,i = heapq.heappop(minHeap)
            if v != prev:
                prev = v
                priority += 1
            ans[i] = priority
        return ans

if __name__ == "__main__":
    arr = [1,4,8,2,4,5,3]
    ans = Solution().minPriority(arr)
    print(ans)
    assert ans == [1,4,6,2,4,5,3]