# https://www.acmicpc.net/problem/1436
# 실버5

N=int(input())
count=0
num=0
while 1:
    num+=1
    if('666' in str(num)):
        count+=1
    if(count == N):
        print(num)
        break
