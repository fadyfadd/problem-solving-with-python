class Solution:
    def Max_Profit(self , prices):
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            current_profit = price - min_price
            max_profit = max(current_profit , max_profit)
            min_price = min(price , min_price)
        
        return max_profit


print(Solution().maxProfit([7,1,5,3,6,4])) #5
print(Solution().maxProfit([7,6,5,4,3,1])) #0
print(Solution().maxProfit([1,2,3,4])) #3
print(Solution().maxProfit([1])) #0
print(Solution().maxProfit([])) #0