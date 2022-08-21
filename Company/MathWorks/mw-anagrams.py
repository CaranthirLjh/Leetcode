# https://www.1point3acres.com/bbs/thread-919688-1-1.html

from collections import Counter, defaultdict

class Solution:
    def funAnagrams(self, words, phrases):
        
        def _genHash(word):
            cnt = Counter(word)
            h = ""
            for c in sorted(cnt):
                h += f"{c}-{cnt[c]};"
            return h
        
        w2h = defaultdict(str)
        h2w = defaultdict(list)

        for word in words:
            h = _genHash(word)
            w2h[word] = h
            h2w[h].append(word)
        
        ans = []
        for phrase in phrases:
            _words = phrase.split(" ")
            cur = 1
            for _w in _words:
                if _w not in w2h:
                    continue
                _h = w2h[_w]
                cur *= len(h2w[_h])
            ans.append(cur)
        return ans

if __name__ == "__main__":
    words = ["west", "has", "good", "stew", "it"]
    phrases = ["west has good stew", "good stew"]
    ans = Solution().funAnagrams(words, phrases)
    assert(ans, [4,2])