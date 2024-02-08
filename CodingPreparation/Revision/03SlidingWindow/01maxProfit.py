def maxProfit(prices):
    left = 0
    right = 1
    maxProfit = float('-inf')
    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxProfit = max(profit, maxProfit)
            
        else:
            left = right
        
        right += 1
    
    return maxProfit

prices = [7,2,1,8,3,9]
print(maxProfit(prices))