def best_time_to_buy_stock(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price: # check if this is a new minimum
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit,profit)
        
    return max_profit
print(best_time_to_buy_stock([7,1,5,3,6,4]))  # Output: 5
print(best_time_to_buy_stock([7,6,4,3,1]))  


