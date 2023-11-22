import heapq as heap

L1 = []

heap.heappush(L1, 25)
heap.heappush(L1, 14)
heap.heappush(L1, 2)
heap.heappush(L1, 20)
heap.heappush(L1, 10)
print(L1)

print(heap.heappop(L1))
print(L1)