# https://www.acmicpc.net/problem/10799
# 실버2
galho=input()
stack=[]
answer=0

for i in range(len(galho)):
    if galho[i] == '(':
        stack.append(galho[i])
    else:
        if galho[i-1] == '(':
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1

print(answer)
