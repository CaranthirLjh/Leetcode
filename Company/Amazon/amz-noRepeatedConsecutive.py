# https://www.1point3acres.com/bbs/thread-921612-1-1.html

class Solution:
    def noRepeatedConsecutive(self, word):
        seen = set()
        l = len(word)
        ans = 0
        for c in word:
            if c in seen:
                ans += 1
                seen = set([c])
            else:
                seen.add(c)
        return ans+1 if seen else ans

if __name__ == "__main__":
    word = "aabcdea"
    ans = Solution().noRepeatedConsecutive(word)
    print(ans)
    assert ans == 3