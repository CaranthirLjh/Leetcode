# https://www.1point3acres.com/bbs/thread-921279-1-1.html

class Solution:
    def buyNovel(self, books):
        mask = 0
        ans = []
        bought = set()
        latest = 0
        for b in books:
            latest = max(latest,b)
            mask |= 1<<(b-1)
            if mask & ((1<<latest)-1) == ((1<<latest)-1):
                cur = []
                for i in range(1,latest+1):
                    if i not in bought:
                        bought.add(i)
                        cur.append(i)
                ans.append(cur)
            else:
                ans.append([-1])
        return ans
    
if __name__ == "__main__":
    books = [1,3,2,4,5]
    ans = Solution().buyNovel(books)
    print(ans)
    assert ans == [[1],[-1],[2,3],[4],[5]]