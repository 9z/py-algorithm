# 실버2
# https://www.acmicpc.net/problem/11279

import sys
import heapq

N=int(input())
heap=[]

for _ in range(N):
    x=int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-1 * heapq.heappop(heap))
    else:
        heapq.heappush(heap, -x)