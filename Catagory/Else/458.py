import math


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        states = minutesToTest // minutesToDie + 1
        ans = math.log(buckets,states)
        return int(ans) if states**int(ans) == buckets else math.ceil(ans)

if __name__ == "__main__":
    buckets = 4
    minutesToDie = 15
    minutesToTest = 30
    ans = Solution().poorPigs(buckets, minutesToDie, minutesToTest)
    assert ans == 2