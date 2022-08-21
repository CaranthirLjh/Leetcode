# 473. Matchsticks to Square

# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

# Return true if you can make this square and false otherwise.

from typing import List
from collections import Counter

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total%4:
            return False
        target = total//4
        counter = Counter(matchsticks)
        
        seen = set()
        
        def _check(cand, cur, counter, remain):
            curMask = ""
            for k in counter:
                curMask += str(k)+"-"+str(counter[k])+";"
            if (cur,remain,curMask) in seen:
                return False
            if cur == target:
                cand = []
                cur = 0
                remain -= 1

            if remain == 0:
                return True
            
            for i in counter:
                if counter[i]>0 and cur+i <= target:
                    cand.append(i)
                    counter[i]-=1
                    if _check(cand, cur+i, counter, remain):
                        return True
                    counter[i]+=1
                    cand.pop()
            
            seen.add((cur, remain, curMask))
            return False
        
        return _check([],0,counter,4)

if __name__  == "__main__":
    matchsticks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    ans = Solution().makesquare(matchsticks)
    assert(ans, True)