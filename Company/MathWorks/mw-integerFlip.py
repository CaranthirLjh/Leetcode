class Solution:
    def integerFlip(self, num: int):
        if num == 1:
            print("1 0")
        seen = {}
        cur = 1
        ans = 0
        offset = 0
        while(cur != 0 and cur not in seen):
            seen[cur] = offset
            ans = ans*10+(10*cur//num)
            cur = 10*cur%num
            offset += 1
        if cur == 0:
            print(f"{ans/(10**offset)} 0")
        else:
            print(f"{ans/(10**offset)} {offset-seen[cur]}")

if __name__ == "__main__":
    num = 12
    Solution().integerFlip(num)
