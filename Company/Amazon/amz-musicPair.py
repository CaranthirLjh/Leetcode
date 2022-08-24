# https://www.1point3acres.com/bbs/thread-922259-1-1.html

from collections import defaultdict

class Solution:
    def musicPair(self, rideDuration, songDurations):
        seen = defaultdict(list)

        target = rideDuration-30
        if target <= 0:
            return []
        
        for i,d in enumerate(songDurations):
            if target-d in seen:
                return [seen[target-d][0],i]
            seen[d].append(i)
        return []

if __name__ == "__main__":
    rideDuration = 90
    songDurations = [1,10,25,35,60]
    ans = Solution().musicPair(rideDuration=rideDuration,songDurations=songDurations)
    print(ans)
    assert(ans, [2,3])