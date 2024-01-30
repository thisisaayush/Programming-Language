def findZigZag(a, n):
    a.sort()
    mid = n // 2
    
    start = mid
    end = n - 1
    
    while start <= end:
        a[start], a[end] == a[end], a[start]
        start += 1
        end -= 1