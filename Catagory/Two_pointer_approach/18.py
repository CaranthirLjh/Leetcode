# 18. 4Sum

# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target

# You may return the answer in any order.

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(nums, target):
            ans = set()
            seen = set()
            for num in nums:
                if target-num in seen:
                    ans.add((target-num,num))
                seen.add(num)
            return ans
        
        def kSum(nums, target, k):
            if k == 2:
                return twoSum(nums, target)
            ans = list()
            avg = target//k
            if avg<nums[0] or avg>nums[-1]:
                return ans
            l = len(nums)
            for i,num in enumerate(nums[:l-k+1]):
                if i==0 or num!=nums[i-1]:
                    candidates = kSum(nums[i+1:], target-num, k-1)
                    for cand in candidates:
                        ans.append(list(cand)+[num])
            return ans
        
        nums.sort()
        return kSum(nums, target, 4)

if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0
    ans = Solution().fourSum(nums, target)
    assert(ans,[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])