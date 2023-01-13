# https://www.acmicpc.net/problem/2812
# 골드3

n, k=map(int, input().split())
number=list(input())
# number=list(map(int, input()))

answer=[]
cnt=k
for num in number:
    while answer and cnt > 0 and answer[-1] < num:
        answer.pop();
        cnt-=1
    answer.append(num)
print(''.join(answer[:n-k]))