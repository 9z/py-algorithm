# https://www.acmicpc.net/problem/3190
# 골드4
from collections import deque

def changeDirection(direction, command):
    if command == 'L':
        return (direction-1) % 4
    elif command == 'R':
        return (direction+1) % 4
    else:
        return direction

# 맵 크기 n x n 입력받기
n=int(input())
# 사과 개수
k=int(input())

# 사과 위치 입력받고 맵에 사과위치 2로 표시
field=[[0] * n for _ in range(n)]
for _ in range(k):
    ax, ay=map(int, input().split())
    field[ax-1][ay-1]=2

turnAfterTime={}
# 특정 시간 후 방향전환 데이터 입력받고 객체형태로 저장
l=int(input())
for _ in range(l):
    second, shift=input().split()
    turnAfterTime[int(second)]=shift

# 0: 위
# 1: 오른쪽
# 2: 아래
# 3: 왼쪽
direction=0

# 0: 위로 이동
# 1: 오른쪽 이동
# 2: 아래쪽 이동
# 3: 왼쪽 이동
dx=[0, 1, 0, -1]
dy=[-1, 0, 1, 0]
x, y=0, 0

time=0

# 자기 몸에 부딪힌다
while 1:
    # 벽에 몸이 부딪힌다
    if n <= x+=dx[d] < 0 | n <= y+=dy[d] < 0:
        break
    x+=dx[d]
    y+=dy[d]
    c=input()
    directiond=changeDirection(direction, c)
    print(x, y)
    time+=time

print(time)