def matchPairs(arr):
    matchPair = {}
    countPairs = 0
    
    for p in arr:
        matchPairs[p] = matchPairs.get(p, 0) + 1
    
    for x in matchPairs.values():
        count += x // 2
    
    return count
        