# 309. Best Time to Buy and Sell Stock with Cooldown

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        sell = [float("-inf")]*(l+1)
        hold = [float("-inf")]*(l+1)
        reset = [0]*(l+1)
        
        for i,p in enumerate(prices):
            sell[i+1] = hold[i]+prices[i]
            hold[i+1] = max(hold[i],reset[i]-prices[i])
            reset[i+1] = max(reset[i],sell[i])
        return max(sell[-1],reset[-1])
    
if __name__ == "__main__":
    prices = [1,2,3,0,2]
    ans = Solution().maxProfit(prices)
    assert(ans,3)