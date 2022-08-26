from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        l = len(nums)
        if l < 3:
            return False
        leftMin = [float("inf")]*l
        leftMin[0] = nums[0]
        for i in range(1,l):
            leftMin[i] = min(leftMin[i-1],nums[i-1])
        
        stack = []
        
        for i in range(l-1,0,-1):
            if nums[i]<=leftMin[i]:
                continue
            while(stack and stack[-1]<=leftMin[i]):
                stack.pop()
            if stack and stack[-1]<nums[i]:
                return True
            stack.append(nums[i])
        return False

if __name__ == "__main__":
    nums = [-1,3,2,0]
    ans = Solution().find132pattern(nums)
    assert ans == True