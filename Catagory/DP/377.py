# 377. Combination Sum IV

# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

# The test cases are generated so that the answer can fit in a 32-bit integer.

from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        l = len(nums)
        dp = [0]*(target+1)
        dp[0] = 1
        
        for i in range(1,target+1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i-num]
        return dp[-1]

if __name__ == "__main__":
    nums = [1,2,3]
    target = 4
    ans = Solution().combinationSum4(nums, target)
    assert(ans,7)