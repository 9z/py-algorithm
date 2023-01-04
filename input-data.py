# 숫자 입력받기

# 한개만 입력받기
# num=int(input())
# 한줄에 띄어쓰기로 변수만큼 여러개 입력받기
# a, b=map(int, input().split())
# 숫자 한개 입력받고 각 자리수마다 배열로 저장하기
# a=list(map(int, input()))
# 한줄에 띄어쓰기로 여러개 입력받고 배열에 저장하기
# a=list(map(int, input().split()))
# range 수만큼 줄바꿈으로 입력받고 각 자리수마다 
# 숫자를 배열로 그리고 그 배열을 2차원 배열로 저장하기
# a=[list(map(int, input())) for _ in range(2)]
# 숫자를 띄어쓰기로 입력받고
# range 수만큼 줄바꿈으로 입력받은 다음
# 2차원 배열에 저장하기
# a=[list(map(int, input().split())) for _ in range(3)]



# 문자열 입력받기

# 문자열 한개 입력받기
# a=input()
# 문자열 한줄에 띄어쓰기로 변수 개수만큼 입력받기
# a, b=input().split()
# range에 설정한 수 만큼 줄바꿈으로 입력받고 배열에 저장
# strings=[input() for _ in range(3)]
# range에 설정한 수만큼 줄바꿈으로 입력받고
# 한줄에 띄어쓰기로 여러개 입력받고 2차원 배열에 저장
# strings=[input().split() for _ in range(3)]

x,y=map(int, input().split())
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)