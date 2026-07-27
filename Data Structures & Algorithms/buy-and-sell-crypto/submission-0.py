class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val=[0]*len(prices)
        max_val=0
        min_val[0]=prices[0]
        for i in range(1,len(prices)):
            min_val[i]=min(prices[i],min_val[i-1])
            max_val=max(max_val,prices[i]-min_val[i-1])
        return max_val