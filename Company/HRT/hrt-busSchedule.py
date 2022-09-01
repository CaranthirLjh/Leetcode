# https://www.1point3acres.com/bbs/thread-921924-1-1.html

# 给bus schedule列表的时间["00:00", "12:00", "17:00"...] 和time="12:30"  求 time与schedule之前的最近时间的差多少分钟
# 这里就是12：30 - 12：00 = 30 分钟， 如果没有找到就返回-1

class Solution:
    def busSchedule(self, bus_schedule, time):
        ans = float("inf")
        h,m = time.split(":")
        h = int(h)
        m = int(m)

        for time in bus_schedule:
            _time = time.split(":")
            _h = int(_time[0])
            _m = int(_time[1])
            gap = abs(abs(h-_h)*60+(m-_m))
            ans = min(ans,gap,23*60+60-gap)
        return ans

if __name__ == "__main__":
    bus_schedule = ["00:00", "12:00", "17:00"]
    time="13:30"
    ans = Solution().busSchedule(bus_schedule, time)
    print(ans)