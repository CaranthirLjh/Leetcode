# https://www.1point3acres.com/bbs/thread-855087-1-1.html

class Solution:
    def shipParcels(self, parcels, k):
        l = len(parcels)
        parcels = set(parcels)
        remain = k-l
        cur = 1
        ans = 0
        while(remain>0):
            if cur not in parcels:
                ans += cur
                remain -= 1
            cur += 1
        return ans

if __name__ == "__main__":
    parcels = [2, 3, 6, 10, 11]
    k = 9
    ans = Solution().shipParcels(parcels,k)
    print(ans)
    assert ans == 17