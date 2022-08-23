# 307. Range Sum Query - Mutable

# Given an integer array nums, handle multiple queries of the following types:

# Update the value of an element in nums.
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# void update(int index, int val) Updates the value of nums[index] to be val.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.l = len(nums)
        self.layer = int(math.log2(2*self.l-1))
        self.seg = [0]*(2**(self.layer+1)-1)
        self._initSeg(0,self.l-1,0)
    
    def _initSeg(self,l,r,ind):
        if l==r:
            self.seg[ind] = self.nums[l]
            return self.seg[ind]
        mid = (l+r)//2
        left = self._initSeg(l,mid,ind*2+1)
        right = self._initSeg(mid+1,r,ind*2+2)
        self.seg[ind] = left+right
        return self.seg[ind]
        
    def update(self, index: int, val: int) -> None:
        if self.nums[index] == val:
            return
        diff = val-self.nums[index]
        self.nums[index] = val
        
        def _update(l,r,ind):
            if index<l or index>r:
                return
            self.seg[ind]+=diff
            if l==r:
                return
            mid = (l+r)//2
            _update(l,mid,ind*2+1)
            _update(mid+1,r,ind*2+2)
        
        _update(0,self.l-1,0)

    def sumRange(self, left: int, right: int) -> int:
        
        def _sum(l,r,ind):
            if left>r or right<l:
                return 0
            if left<=l and right>=r:
                return self.seg[ind]
            mid = (l+r)//2
            return _sum(l,mid,ind*2+1)+_sum(mid+1,r,ind*2+2)
        
        return _sum(0,self.l-1,0)
            