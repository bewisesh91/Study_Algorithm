from collections import deque
queue = deque()

queue.append('승현')
queue.append('문승현')
queue.append('합격')

print(queue[0])
print(queue.popleft())
print(queue)