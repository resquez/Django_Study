# 리스트(list)
# 순서가 있는 가변 시퀀스 타입
empty_list = []
numbers = [1, 2, 3, 4, 5]
strings = ['Hello', 'World']
# 여러 데이터 타입을 혼합하여 저장할 수 있음
mixed = [1, 'Hello', 3.14, True, [1, 2, 3], {'name': 'Alice'}]

# 튜플(tuple)
# 순서가 있는 불변 시퀀스 타입
empty_tuple = ()
numbers = (1, 2, 3, 4, 5)
strings = ('Hello', 'World')
# 여러 데이터 타입을 혼합하여 저장할 수 있음
mixed = (1, 'Hello', 3.14, True, [1, 2, 3], {'name': 'Alice'})

# 하나의 데이터만 가지는 튜플은 콤마(,)를 붙여야 함
single = (1,)
print(type(single))  # <class 'tuple'>


# 콤마(,)를 붙이지 않으면 int 타입(또는 다른 데이터 타입)으로 인식
single = (1)
print(type(single))  # <class 'int'>