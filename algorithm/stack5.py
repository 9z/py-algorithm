# https://www.acmicpc.net/problem/1406
# 실버2

# input() 보단 stdin 이 훨씬 빠르므로 왠만하면 stdin을 이용하자
from sys import stdin

inputString=list(stdin.readline().strip())
n=int(input())

stack=[]

for _ in range(n):
    # 명령어를 한번에 다 입력받아놓고 반복문을 사용하는 것 보다 반복하면서 입력 받는게 더 빠름
    command=stdin.readline().split()
    if command[0]=='L':
        if len(inputString)>0:
            stack.append(inputString.pop())
    elif command[0]=='D':
        if len(stack)>0:
            inputString.append(stack.pop())
    elif command[0]=='B':
        if len(inputString):
            inputString.pop()
    elif command[0]=='P':
        inputString.append(command[1])

print(''.join(inputString)+''.join(list(reversed(stack))))