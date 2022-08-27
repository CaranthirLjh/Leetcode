from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def _merge(left,mid,right):
            l = left
            r = mid+1
            ans = 0
            offset = mid+1
            for i in range(left,mid+1):
                while(offset<=right and nums[i]>2*nums[offset]):
                    offset += 1
                ans += (offset-mid-1)
            tmp = []
            while(l<=mid or r<=right):
                if l == mid+1:
                    tmp.append(nums[r])
                    r+=1
                elif r == right+1:
                    tmp.append(nums[l])
                    l+=1
                else:
                    if nums[l]<nums[r]:
                        tmp.append(nums[l])
                        l+=1
                    else:
                        tmp.append(nums[r])
                        r+=1
            for i in range(len(tmp)):
                nums[left+i] = tmp[i]
            return ans
        
        def _merge_sort(left,right):
            if left >= right:
                return 0
            mid = (left+right)//2
            ans = _merge_sort(left,mid)
            ans += _merge_sort(mid+1,right)
            ans += _merge(left,mid,right)
            return ans
        
        return _merge_sort(0,len(nums)-1)

if __name__ == "__main__":
    nums = [2,4,3,5,1]
    ans = Solution().reversePairs(nums)
    assert ans == 3