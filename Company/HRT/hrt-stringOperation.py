# https://www.1point3acres.com/bbs/thread-923849-1-1.html


class Solution:
    def stringOperation(self, operations):
        ans = []
        cache = []

        for op in operations:
            ops = op.split(" ")
            if not ops:
                continue
            prev = cache[-1] if cache else ""
            if ops[0] == "INSERT":
                if len(op) == 6:
                    cur = prev
                else:
                    cur = prev+op[7:]
                ans.append(cur)
                cache.append(cur)
            elif ops[0] == "BACKSPACE":
                if not cache:
                    ans.append("")
                else:
                    prev = cache[-1]
                    if prev:
                        prev = prev[:-1]
                        cache.append(prev)
                    ans.append(prev)
                    
            elif ops[0] == "UNDO":
                if not cache:
                    ans.append("")
                else:
                    cache.pop()
                    cur = "" if not cache else cache[-1]
                    ans.append(cur)
        return ans

if __name__ == "__main__":
    operations = ["BACKSPACE", "UNDO", "INSERT test1", "BACKSPACE", "BACKSPACE", "BACKSPACE", "UNDO","INSERT test2","UNDO"]
    ans = Solution().stringOperation(operations)
    print(ans)