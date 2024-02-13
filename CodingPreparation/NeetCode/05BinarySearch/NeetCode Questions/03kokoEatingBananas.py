import math

def minEatingRate(piles, h):
    left = 1
    right = max(piles)
    result = right # this is because, the max value from the piles will definitely work.
    
    
    while left <= right:
        k = (left + right) // 2
        hours = 0
        
        for p in piles:
            hours += math.ceil(p / k) # O(n) for each piles to find best k.
            
        if hours <= h:
            result = min(result, k)
            right = k - 1
        
        else:
            left = k + 1
    
    return result