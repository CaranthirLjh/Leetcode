# 1696. Jump Game VI

# You are given a 0-indexed integer array nums and an integer k.

# You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

# You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

# Return the maximum score you can get.

from typing import List
from collections import deque

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        l = len(nums)
        scores = [float("-inf")]*l
        candidates = deque([0])
        
        scores[0] = nums[0]
        
        for i in range(1,l):
            while(candidates and candidates[0]<i-k):
                candidates.popleft()
            scores[i] = scores[candidates[0]]+nums[i]
            
            while(candidates and scores[candidates[-1]]<scores[i]):
                candidates.pop()
            candidates.append(i)
        
        return scores[-1]

if __name__ == "__main__":
    nums = [10,-5,-2,4,0,3]
    k = 3
    ans = Solution().maxResult(nums, k)
    assert(ans, 17)
