# 472. Concatenated Words

# Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

# A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        cache = set()
        
        def _backtrace(word, offset, concat):
            if offset == len(word):
                return True
            if concat[offset] or word[offset:] in cache:
                return True
            for i in range(offset,len(word)):
                if word[offset:i+1] in wordSet and (offset,i+1) != (0,len(word)):
                    if _backtrace(word, i+1, concat):
                        concat[offset] = True
                        return True
            return False
        
        ans = []
        for word in words:
            l = len(word)
            concat = [False]*l
            if _backtrace(word,0,concat):
                cache.add(word)
                ans.append(word)
        return ans

if __name__ == "__main__":
    words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    ans = Solution().findAllConcatenatedWordsInADict(words)
    assert ans == ["catsdogcats","dogcatsdog","ratcatdogcat"]