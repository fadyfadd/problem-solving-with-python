def max_profit(prices):
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            current_profit = price - min_price
            max_profit = max(current_profit , max_profit)
            min_price = min(price , min_price)
        
        return max_profit

print(max_profit([7,1,5,3,6,4])) #5
print(max_profit([7,6,5,4,3,1])) #0
print(max_profit([1,2,3,4])) #3
print(max_profit([1])) #0
print(max_profit([])) #0