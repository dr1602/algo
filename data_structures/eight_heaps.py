import heapq

heap = []

heapq.heappush(heap, 3)
print(heap)
# [3]

heapq.heappush(heap, 1)
print(heap)
# [1, 3]

heapq.heappush(heap, 4)
print(heap)
# [1, 3, 4]

print(heapq.heappop(heap))
# 1