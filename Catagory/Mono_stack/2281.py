# 2281. Sum of Total Strength of Wizards

# As the ruler of a kingdom, you have an army of wizards at your command.

# You are given a 0-indexed integer array strength, where strength[i] denotes the strength of the ith wizard. For a contiguous group of wizards (i.e. the wizards' strengths form a subarray of strength), the total strength is defined as the product of the following two values:

# The strength of the weakest wizard in the group.
# The total of all the individual strengths of the wizards in the group.
# Return the sum of the total strengths of all contiguous groups of wizards. Since the answer may be very large, return it modulo 109 + 7.

# A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List
from itertools import accumulate

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        mod = 10**9+7
        l = len(strength)
        
        right = [l]*l
        stack = []
        for i,val in enumerate(strength):
            while(stack and strength[stack[-1]]>val):
                right[stack.pop()] = i
            stack.append(i)
        
        left = [-1]*l
        stack = []
        for i in range(l-1,-1,-1):
            while(stack and strength[stack[-1]]>=strength[i]):
                left[stack.pop()] = i
            stack.append(i)
        
        ans = 0
        prefix = list(accumulate(accumulate(strength), initial = 0))
        
        for i in range(l):
            l,r = left[i],right[i]
            l_acc = prefix[i]-prefix[max(0,l)]
            r_acc = prefix[r]-prefix[i]
            ans = (ans+strength[i]*(r_acc*(i-l)-l_acc*(r-i)))%mod
        return ans

if __name__ == "__main__":
    strength = [1,3,1,2]
    ans = Solution().totalStrength(strength)
    assert(ans,44)