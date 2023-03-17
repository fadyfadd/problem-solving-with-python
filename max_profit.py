class solution:
    def maxProfit(self , prices:list[int]) -> int:
        max_profit:int = 0
        min_price:int = float('inf')

        for price in prices:
            current_profit = price - min_price
            max_profit = max(current_profit , max_profit)
            min_price = min(price , min_price)
        
        return max_profit


print(solution().maxProfit([7,1,5,3,6,4])) #5
print(solution().maxProfit([7,6,5,4,3,1])) #0
print(solution().maxProfit([1,2,3,4])) #3
print(solution().maxProfit([1])) #0
print(solution().maxProfit([])) #0