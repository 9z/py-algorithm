# https://www.acmicpc.net/problem/3190
# 골드4
from collections import deque

def changeDirection(direction, command):
    if command == 'L':
        return (direction-1) % 4
    else:
        return (direction+1) % 4

# 맵 크기 n x n 입력받기
n=int(input())
# 사과 개수
k=int(input())
field=[[0] * n for _ in range(n)]

# 사과 위치 입력받고 맵에 사과위치 1로 표시
for _ in range(k):
    ax, ay=map(int, input().split())
    field[ax-1][ay-1]=1

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
direction=1

# 0: 위로 이동
# 1: 오른쪽 이동
# 2: 아래쪽 이동
# 3: 왼쪽 이동
dy=[-1, 0, 1, 0]
dx=[0, 1, 0, -1]
y, x=0, 0

time=1

snake=deque([[y,x]])
field[y][x]=2

while 1:
    y, x = y + dy[direction], x + dx[direction]
    if 0 <= y < n and 0 <= x < n and field[y][x] != 2:
        if not field[y][x] == 1:
            delY, delX=snake.popleft()
            field[delY][delX] = 0
        field[y][x]=2
        snake.append([y, x])
        if time in turnAfterTime.keys():
            direction=changeDirection(direction, turnAfterTime[time])
        time += 1
    # 자기 몸에 부딪힌다
    # 벽에 몸이 부딪힌다
    else:
        break

print(time)