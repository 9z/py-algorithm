from collections import deque

snake=deque([[1, 2], [5, 4]])

print(snake.appendleft([3, 3]))
print(snake)

# 뒤쪽 기준
# append(), pop()

# 앞쪽 기준
# appendleft(), popleft()