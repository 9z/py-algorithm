# https://www.acmicpc.net/problem/3190
# 골드4

def changeDirection(direction, command):
    if command == 'L':
        return (direction-1) % 4
    elif command == 'R':
        return (direction+1) % 4
    else:
        return direction

n=int(input())
k=int(input())
print(n, k)
# 0: 위
# 1: 오른쪽
# 2: 아래
# 3: 왼쪽
d=0

# 0: 위로 이동
# 1: 오른쪽 이동
# 2: 아래쪽 이동
# 3: 왼쪽 이동
dx=[0, 1, 0, -1]
dy=[-1, 0, 1, 0]
x, y=0, 0
field=[[0] * 10 for _ in range(10)]

# while 1:
#     c=input()
#     d=changeDirection(d, c)
#     x+=dx[d]
#     y+=dy[d]
#     print(x, y)
