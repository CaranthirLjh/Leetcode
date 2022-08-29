from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        start = float("inf")
        
        for i,num in enumerate(nums):
            while(stack and stack[-1][0]>num):
                start = min(start,stack.pop()[1])
            stack.append((num,i))
        
        if start == float("inf"):
            return 0
        
        stack = []
        l = len(nums)
        end = float("-inf")
        for i in range(l-1,-1,-1):
            num = nums[i]
            while(stack and stack[-1][0]<num):
                end = max(end,stack.pop()[1])
            stack.append((num,i))
        return end-start+1

if __name__ == "__main__":
    nums = [2,6,4,8,10,9,15]
    ans = Solution().findUnsortedSubarray(nums)
    assert ans == 5