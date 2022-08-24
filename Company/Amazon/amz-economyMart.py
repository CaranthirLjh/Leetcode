# https://www.1point3acres.com/bbs/thread-922259-1-1.html

import heapq

class Solution:
    def economyMart(self, entries):
        minHeap = []
        maxHeap = []
        readCount = 0
        ans = []
        for e in entries:
            op, item, price = e
            if op == "INSERT":
                if not minHeap or (len(maxHeap) == readCount and price >= minHeap[0][0]):
                    heapq.heappush(minHeap,(price,item))
                else:
                    heapq.heappush(maxHeap,(-price,item))
                    while len(maxHeap)>readCount:
                        _price,_item = heapq.heappop(maxHeap)
                        heapq.heappush(minHeap,(-_price,_item))
            elif op == "VIEW":
                ans.append(minHeap[0][1])
                readCount += 1
                while(len(maxHeap)<readCount):
                    _price,_item = heapq.heappop(minHeap)
                    heapq.heappush(maxHeap,(-_price,_item))
        return ans
    
if __name__ == "__main__":
    entries = [
        ["INSERT", "coffee",3], 
        ["INSERT", "milk",4],
        ["VIEW", "-", "-"],
        ["INSERT", "gum",1], 
        ["INSERT", "pizza",5],
        ["VIEW", "-", "-"],
    ]
    ans = Solution().economyMart(entries=entries)
    print(ans)
    assert(ans,["coffee","coffee"])