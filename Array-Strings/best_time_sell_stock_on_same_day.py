def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        # if today's price is greater than yesterday's price , sell today
        if prices[i] > prices[i - 1]: 
            profit += prices[i] - prices[i - 1]
    return profit
print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
print(maxProfit([1,2,3,4,5]))

# You have take stocks for rupee 7 yesterday and today's stock rate is 1 , so we should not sell in order to get profit
#if you bought stock for 1 rupee and today's rate for that stock is 5 rupee, if you sell stock you get profit . So it is best time to sell stock