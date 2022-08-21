# 84. Largest Rectangle in Histogram

# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(-1,-1)]
        ans = 0
        for i,h in enumerate(heights):
            while(h < stack[-1][0]):
                _h,_i = stack.pop()
                ans = max(ans,_h*(_i-stack[-1][1]+(i-1-_i)))
            stack.append((h,i))
        i = len(heights)
        while(len(stack)>1):
            _h,_i = stack.pop()
            ans = max(ans,_h*(_i-stack[-1][1]+(i-1-_i)))
        return ans

if __name__ == "__main__":
    heights = [2,1,5,6,2,3]
    ans = Solution().largestRectangleArea(heights)
    assert(ans, 10)