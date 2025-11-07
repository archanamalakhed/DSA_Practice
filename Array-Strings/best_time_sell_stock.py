def best_time_to_buy_stock(prices):
    #SINGLE TRANSCATION VERSION
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price: # check if this is a new minimum,  New lowest price → best day to buy
            min_price = price # always prefer to buy stock at min value so set min value first
        else:
            profit = price - min_price
            max_profit = max(max_profit,profit) # Potential profit if sold today
        
    return max_profit
print(best_time_to_buy_stock([7,1,5,3,6,4]))  # Output: 5
print(best_time_to_buy_stock([7,6,4,3,1]))  

# positive inf is always higher number than any value 7 is less than positive inf first min value will be set to 7


