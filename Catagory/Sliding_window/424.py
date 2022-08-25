from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = len(s)
        left = 0
        ans = 0
        for right,c in enumerate(s):
            count[c] += 1
            while(right-left+1-max(count.values())>k):
                count[s[left]]-=1
                left+=1
            ans = max(ans,right-left+1)
        return ans

if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    ans = Solution().characterReplacement(s,k)
    assert ans == 4