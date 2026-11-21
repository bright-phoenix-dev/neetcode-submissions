class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        buy=0
        hold=0
        sell=0
        for i in range(n):
            if i==0:
                buy=-prices[i]
            else:
                buy=max(buy,hold-prices[i])
                hold=max(hold,sell)
                sell=buy+prices[i]
        return max(hold,sell)