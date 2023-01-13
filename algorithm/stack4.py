# https://www.acmicpc.net/problem/9012
# 실버4

n = int(input())

for i in range(n):
    ps=input()
    stack=[]
    end=0
    for char in ps:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0:
                print('NO')
                end=1
                break
            else:
                stack.pop()
    if end == 0:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
    

