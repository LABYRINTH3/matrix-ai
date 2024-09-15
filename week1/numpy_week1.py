import numpy as np

# np.array 배열을 만듬 다양한 수학적 공식 사용가능 / 2차원 배열도 사용가능
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b) # 결과 : [5 7 9]
print(a*b) # 결과 : [4 10 18]
print(a**2) # 결과 : [1 4 9]
print(a % 2 == 0) # 결과 : [False True False]

# dimension / 차원 배열의 차원
a1 = np.array([1,2,3])
print(a1.ndim) # 결과 : 1
a2 = np.array([[1,2],[3,4]])
print(a2.ndim) # 결과 : 2

#차원 크기 확인 하는 코드
a1 = np.array([
	[1,2,3],
	[4,5,6]
])
print(a1.shape) # 결과 : (2,3)

#차원 크기도 변경 가능 - 그냥 차원을 행렬로 생각해도 무방할것으로 보임
a1 = np.array([
	[1,2,3],
	[4,5,6]
])
print(a1)
print(a1.shape) # 결과 : (2,3)

a2 = a1.reshape((1,6))
print(a2)
print(a2.shape)

a3 = a1.reshape((3,2))
print(a3)
print(a3.shape)

#원하는 자료 뽑아내기
a = np.array([
	[1,2,3],
	[4,5,6],
])
print(a[0])
print(a[0,1]) # 결과 : 2 / 행렬과 같음 시작행이 단 시작행이 0임

# range를 이용해서 배열을 만드는것도 가능
a= np.array([
	list(range(10)),
	list(range(10,20))
])
print(a)
#[[ 0  1  2  3  4  5  6  7  8  9]
# [10 11 12 13 14 15 16 17 18 19]]

# 데이터를 이렇게 빼내는것도 가능
print(a[1, [2,3,4]])
#[12 13 14]

# 행 전체를 선택하는건 ":" 사용
print(a[:,2]) # 결과 : [3,6]

array1d = np.arange(1,10)
# 배열 내 요소 검사하는 방법
print(array1d>5)
#[False False False False False  True  True  True  True]

# 조건에 맞는 데이터를 출력 하는 방법
print(array1d[array1d>5])
#[6 7 8 9]
print(array1d[(array1d>5) & (array1d<8)])
#[6 7]

# 배열끼리 결합
# `np.hstack(a1,a2)`  : 좌우로 붙임
# `np.vstack(a1,a2)`  : 위아래로 붙임
# `np.dstack(a1,a2)`  : 가장 안쪽 차원에 대해 붙임
# `np.stack(a1,a2,axis)` : 지정한 축에 대해서 붙임

# 간단한 배열 쉽게 만들기
# `np.ones(shape)` : 지정된 shape을 가지는 1로 이루어진 배열
# `np.zeros(shape)`  : 위와 같지만 0으로 이루어짐
# `np.empty(shape)` : 위와 같지만 값을 초기화하지 않음. 값 자체는 상관없지만 큰 배열을 만들 때 사용

# `np.arange(start,end,step)`  : python의 range와 같은 문법
print(np.arange(1,10)) # 1, 2, 3, 4, 5, 6, 7, 8, 9
print(np.arange(1,10,2)) # 1, 3, 5, 7, 9

# np.linspace(start, end , count) : start 에서 end 까지의 구간을 count 개로 등분
# 1~10까지 10등분을 하는 코드
print(np.linspace(1,10,10)) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

print(np.linspace(0,10,4)) # 0, 3.3333... , 6.66666 , 10

### 난수 배열들

# `np.random.seed(seed)` : RNG의 seed 값 설정

# `np.random.rand(차원1, 차원2, ...)` : 각 차원의 크기를 가진 0~1 사이 난수 배열
np.random.rand(3,3)

# np.random.randn(차원1, 차원2, ...) : 각 인자에 해당하는 크기의 표준정규분포를 따르는 난수 배열
np.random.randn(10,10)

# `np.random.randint(low, high, shape)` : shape 형태의 low~high 사이의 정수를 가진 배열
np.random.randint(1,10,(3,3,10,10))