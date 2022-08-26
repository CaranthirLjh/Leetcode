from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        l,r = 0,10**9//2
        houses.sort()
        heaters.sort()
        house_l, heater_l = len(houses),len(heaters)
        
        def _isValid(rad):
            house_ind,heater_ind = 0,0
            while(house_ind<house_l and heater_ind<heater_l):
                if abs(houses[house_ind]-heaters[heater_ind])<=rad:
                    house_ind+=1
                else:
                    heater_ind+=1
            return house_ind == house_l
        
        while(l<r):
            mid = (l+r)//2
            if _isValid(mid):
                r = mid
            else:
                l = mid+1
        return l

if __name__ == "__main__":
    houses = [1,2,3,4]
    heaters = [1,4]
    ans = Solution().findRadius(houses, heaters)
    assert ans == 1