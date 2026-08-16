class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      #  min_price=float('inf')
       # max_profit=0
       # for price in prices:
          #  if price<min_price:
          #      min_price=price
          #  profit=price-min_price
          #  if profit>max_profit:
           #     max_profit=profit
       # return max_profit 
        l,r=0,1
        max_profit=0
        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                if max_profit<profit:
                    max_profit=profit
            else:
                l=r
            r+=1

        return max_profit
           



