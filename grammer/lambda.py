# def 으로 함수 정의하는 대신 사용할 수 있는 함수 정의법
# lambda 매개변수...: 반환값

# x를 입력받고 x에 2를 곱하여 반환
mulTwo = lambda x: x*2
mulTwo(3) # 결과: 6

# x, y를 입력받고 더하여 반환
add = lambda x, y: x+y
add(10, 30) # 결과 40

# 다른 모듈과 함께 사용하는 방법

# map함수의 첫번재 인자인 람다 함수로 
# 두번째 인자의 배열 각 요소마다 적용함
# map 함수는 결과로 map 객체를 반환하므로 list 함수를 사용해서 배열로 변환
addTen = list(map(lambda x: x +10, [1, 2, 3, 4]))
# print(addTen) # [11, 12, 13, 14]

# sort에서 정렬 기준을 정할때도 사용할 수 있다.
# 각 요소를 인자로 받아서 그 요소의 첫번째 요소(x[0])를 기준으로 정렬하고
# 같으면 두번째 요소(x[1])을 기준으로 정렬시킨다.
array=[[3, 2], [1, 2], [1, 3], [5, 3], [3, 1]]
array.sort(key=lambda x: (x[0], x[1]))
print(array)