# https://www.acmicpc.net/submit/2164
# 실버4

from collections import deque

n=int(input())
queue=deque([])

for i in range(n):
    queue.append(i+1)

        
i = 1
while len(queue) > 1:
    if i%2 == 1:
        queue.popleft()
    else:
        queue.append(queue.popleft())
    i+=1

print(queue.pop())