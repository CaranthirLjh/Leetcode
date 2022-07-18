# 41. First Missing Positive

# Given an unsorted integer array nums, return the smallest missing positive integer.

# You must implement an algorithm that runs in O(n) time and uses constant extra space.

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        if 1 not in nums:
            return 1
        
        for i in range(l):
            if nums[i]<=0 or nums[i]>l:
                nums[i] = 1
        
        for i in range(l):
            cur = abs(nums[i])
            if cur == l:
                nums[0] = -abs(nums[0])
            else:
                nums[cur] = -abs(nums[cur])
        
        for i in range(1,l):
            if nums[i]>0:
                return i
        
        if nums[0]>0:
            return l
        
        return l+1

if __name__ == "__main__":
    nums = [3,4,-1,1]
    ans = Solution().firstMissingPositive(nums)
    assert(ans,2)