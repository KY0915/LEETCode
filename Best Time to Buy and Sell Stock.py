class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0       
        n=len(prices)
        
        # if the list is shorter than 2, just return 0
        if n < 2:
            return maxProfit
        minPrice=prices[0]

        #find and update the minimum price in the list and find current profit and update the max profit.
        for i in prices:
            currProfit=i-minPrice
            if i < minPrice:
                minPrice=i            
            if currProfit>maxProfit:
                maxProfit=currProfit

        return maxProfit
            
            
        
