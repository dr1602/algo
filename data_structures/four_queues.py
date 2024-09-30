from collections import deque

queue = deque()

queue.append(1)
print(queue)
# deque([1])

queue.append(2)
print(queue)
# deque([1, 2])

queue.append(3)
print(queue)
# deque([1, 2, 3])

print(queue.popleft())
# 1
print(queue)
# deque([2, 3])
