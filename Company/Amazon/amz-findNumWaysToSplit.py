# Given a string s and integer num, return number of way to split the string into two substring 

# and the two substring share at least num number of distinct characters

class Solution:
    def findNumWaysToSplit(self, s: str, num: int) -> int:
        l = len(s)
        ans = 0
        for i in range(num,l-num+1):
            prefix = s[:i]
            suffix = s[i:]
            if len(set(prefix) & set(suffix))>num:
                ans += 1
        return ans

if __name__ == "__main__":
    s = "abbcac"
    num = 1
    ans = Solution().findNumWaysToSplit(s, num)
    assert(ans,2)