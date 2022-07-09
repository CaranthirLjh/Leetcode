# 4. Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1,l2 = len(nums1),len(nums2)
        if l1 > l2:
            l1,nums1,l2,nums2 = l2,nums2,l1,nums1
        
        left,right = 0,l1
        mid = (l1+l2+1)//2
        while(left<=right):
            i = (left+right+1)//2
            j = mid-i
            
            if(i>0 and nums1[i-1]>nums2[j]):
                right = i-1
            elif(i<l1 and nums1[i]<nums2[j-1]):
                left = i+1
            else:
                if i == 0:
                    leftMax = nums2[j-1]
                elif j == 0:
                    leftMax = nums1[i-1]
                else:
                    leftMax = max(nums1[i-1],nums2[j-1])
                if (l1+l2)%2:
                    return leftMax
                
                if i == l1:
                    rightMin = nums2[j]
                elif j == l2:
                    rightMin = nums1[i]
                else:
                    rightMin = min(nums1[i],nums2[j])
                return (leftMax+rightMin)/2

if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = [3,4]
    ans = Solution().findMedianSortedArrays(nums1, nums2)
    assert(ans, 2.5)

