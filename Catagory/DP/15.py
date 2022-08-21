# 15. 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

from typing import List
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dup = set()
        seen = defaultdict(int)
        ans = set()
        
        for i,num1 in enumerate(nums):
            if num1 in dup:
                continue
            dup.add(num1)
            for num2 in nums[i+1:]:
                target = -num1-num2
                if target in seen and seen[target] == i:
                    ans.add(tuple(sorted([num1,num2,target])))
                seen[num2] = i
        return ans

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    ans = Solution().threeSum(nums)
    assert(ans, [[-1,-1,2],[-1,0,1]])