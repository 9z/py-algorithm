# 실버1
# https://www.acmicpc.net/problem/1931

N=int(input())
meet=[list(map(int, input().split())) for _ in range(N)]

meet.sort(key=lambda x: (x[1], x[0]))

result=0
endtime=0
for i in range(len(meet)):
    if endtime <= meet[i][0]:
        endtime=meet[i][1]
        result += 1

print(result)