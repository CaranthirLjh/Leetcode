# 719. Find K-th Smallest Pair Distance

# The distance of a pair of integers a and b is defined as the absolute difference between a and b.

# Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        def _possible(guess):
            left,count = 0,0
            for right,num in enumerate(nums):
                while(num-nums[left]) > guess:
                    left+=1
                count += (right-left)
            return count >= k
        
        nums.sort()
        lo = 0
        hi = nums[-1]-nums[0]
        while(lo<hi):
            mid = (lo+hi)//2
            if _possible(mid):
                hi = mid
            else:
                lo = mid+1
        return lo

if __name__ == "__main__":
    nums = [1,6,1]
    k = 3
    ans = Solution().smallestDistancePair(nums,k)
    assert(ans,5)