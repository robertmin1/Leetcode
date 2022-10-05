class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low,curr = 0,1
        Mpro = 0
        while curr < len(prices):
            if prices[low] < prices[curr]:
                profit = prices[curr] - prices[low]
                Mpro = max(profit,Mpro)
            else:
                low = curr
            curr+=1
        return Mpro