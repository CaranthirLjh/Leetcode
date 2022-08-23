# 376. Wiggle Subsequence

# A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

# For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.
# In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The first is not because its first two differences are positive, and the second is not because its last difference is zero.
# A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

# Given an integer array nums, return the length of the longest wiggle subsequence of nums.

from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        l = len(nums)
        up = [1]*l
        down = [1]*l
        for i in range(1,l):
            if nums[i]>nums[i-1]:
                up[i] = down[i-1]+1
                down[i] = down[i-1]
            elif nums[i]<nums[i-1]:
                down[i] = up[i-1]+1
                up[i] = up[i-1]
            else:
                down[i] = down[i-1]
                up[i] = up[i-1]
        return max(down[-1],up[-1])

if __name__ == "__main__":
    nums = [1,17,5,10,13,15,10,5,16,8]
    ans = Solution().wiggleMaxLength(nums)
    assert(ans,7)