# 골드4
# https://www.acmicpc.net/problem/1715

import heapq
N=int(input())

# minHeap=[]
# for _ in range(N):
#     heapq.heappush(minHeap, int(input()))

minHeap = list(int(input()) for _ in range(N))
heapq.heapify(minHeap)

result=0;

# 이렇게 작성할 경우 대부분의 입력에는 맞지만 N이 1일때 에러가 난다.
# sum을 구할때 N이 1이면 두번째 heappop을 할 수가 없어서 IndexError가 발생한다.
# 테스트할때 반드시 입력이 1개인 데이터로 테스트를 해야한다.
# for i in range(len(minHeap)):
#     sum = heapq.heappop(minHeap) + heapq.heappop(minHeap)
#     result += sum
#     heapq.heappush(minHeap, sum)
#     if len(minHeap) == 1:
#         break

while len(minHeap) != 1:
    sum = heapq.heappop(minHeap) + heapq.heappop(minHeap)
    result += sum
    heapq.heappush(minHeap, sum)

print(result)