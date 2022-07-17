# 31. Next Permutation

# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        i = len(nums)-2
        while(i>=0 and nums[i+1]<=nums[i]):
            i -= 1
        if i>=0:
            j = len(nums)-1
            while(nums[j]<=nums[i]):
                j-=1
            nums[i],nums[j] = nums[j],nums[i]
            
        start,end = i+1,len(nums)-1
        while(start<end):
            nums[start],nums[end] = nums[end],nums[start]
            start += 1
            end -= 1
        return nums

if __name__ == "__main__":
    nums = [1,1,5]
    ans = Solution().nextPermutation(nums)
    assert(ans, [1,5,1])