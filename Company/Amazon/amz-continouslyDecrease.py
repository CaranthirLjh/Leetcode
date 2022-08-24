# 给一个list，问里面有多少组连续递减且差值为1的数，return个数。

from typing import List

class Solution:
    def count_continous_decrease(self, scores: List):
        ans = 0
        count = 1
        l = len(scores)
        for i in range(l):
            if i>0 and scores[i] == scores[i-1]-1:
                count += 1
            else:
                count = 1
            ans += count
        return ans

if __name__ == "__main__":
    scores = [4,3,5,4,3]
    ans = Solution().count_continous_decrease(scores)
    assert(ans,9)