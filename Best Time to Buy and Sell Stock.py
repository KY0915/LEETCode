class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0       
        n=len(prices)
        if n < 1:
            return maxProfit
        minPrice=prices[0]

        for i in prices:
            currProfit=i-minPrice
            if i < minPrice:
                minPrice=i            
            if currProfit>maxProfit:
                maxProfit=currProfit

        return maxProfit
            
            
        
