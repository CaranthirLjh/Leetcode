# 30. Substring with Concatenation of All Words

# You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

# You can return the answer in any order.

from typing import List
from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = list()
        l_s = len(s)
        l_w = len(words[0])
        l_substr = len(words[0])*len(words)
        
        def _slidingWindow(offset):
            word_found = 0
            extra_word = False
            word_remain = Counter(words)
            left = offset
            for right in range(left,l_s,l_w):
                if right + l_w > l_s:
                    break
                
                curS = s[right:right+l_w]
                if curS not in word_remain:
                    word_found = 0
                    word_remain = Counter(words)
                    extra_word = False
                    left = right+l_w
                else:
                    while right-left == l_substr or extra_word:
                        leftS = s[left:left+l_w]
                        left += l_w
                        word_remain[leftS]+=1
                        
                        if word_remain[leftS]==0:
                            extra_word = False
                        else:
                            word_found -= 1
                    word_remain[curS]-=1
                    if word_remain[curS]<0:
                        extra_word = True
                    else:
                        word_found += 1
                    if word_found == len(words):
                        ans.append(left)
        
        for i in range(l_w):
            _slidingWindow(i)
        return ans
                    
if __name__ == "__main__":
    s = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]
    ans = Solution().findSubstring(s, words)
    assert(ans, [6,9,12])