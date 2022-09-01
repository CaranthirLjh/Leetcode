# https://www.1point3acres.com/bbs/thread-921924-1-1.html

# 给query ['+2', '-1', '+3' ...] 和 diff = 1，+号是将一个该数字放入，-号是删除所有的这个数字，返回一个‍‌‌‌‍‌‍‌‍‌‌‍‌‍‍‌‌‍‍‌等于query长度的int 列表，每个int表示当前query放入或删除数字后，总共有多少pairs （两个数字）相差 diff
# ['+2', '+1', '+3', '-1', '+2', '-2']， diff = 1 返回答案 [0, 1, 2, 1, 2, 0]
# 解释：+2 得到 [2] 没有相差1的pair，result= [0]
# +1 得到 [2, 1] 2和1相差1,总共1对pair， result= [0，1]
# +3 得到 [2, 1, 3] 相比之前，多了 2，3pair， 多1对pair， result= [0, 1, 2]
# -1  删除所有的数字1， 得到 [2, 3] 少了一对， result=[0,1,2,1] 以此类推

from collections import defaultdict


class Solution:
    def findNumWithKDiff(self, query, k):
        counter = defaultdict(int)
        ans = []
        cur = 0
        for q in query:
            op = q[0]
            num = int(q[1:])
            if op == "+":
                counter[num] += 1
                cur += (counter[num-k]+counter[num+k])
            elif op == "-":
                cur -= counter[num]*(counter[num-k]+counter[num+k])
                counter[num] = 0
            ans.append(cur)
        return ans

if __name__ == "__main__":
    query = ['+2', '+1', '+3', '-1', '+2', '-2']
    k = 1
    ans = Solution().findNumWithKDiff(query,k)
    print(ans)
