# 실버3
# https://www.acmicpc.net/problem/9375

C=int(input())
for _ in range(C):
    cloths={}
    n=int(input())
    for _ in range(n):
        name, category=input().split()
        if category in cloths:
            cloths[category] += 1
        else:
            cloths[category] = 1
    result=1
    for key in cloths.keys():
        result *= (cloths[key]+1)

    print(result-1)