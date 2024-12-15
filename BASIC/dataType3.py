# 범위(range)
# 불변 시퀀스 타입
# 리스트와 달리 시작, 종료, 단계(step) 값만 저장하고, 실제 값은 필요할 때마다 생성하는 방식으로 동작

a = range(10)       # 0부터 9까지의 범위
print(a)            # range(0, 10)
print(list(a))      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


a = range(5, 10)    # 5부터 9까지의 범위
print(a)            # range(5, 10)
print(list(a))      # [5, 6, 7, 8, 9]


a = range(2, 10, 2) # 2부터 9까지의 범위, 단계는 2
print(a)            # range(2, 10, 2)
print(list(a))      # [2, 4, 6, 8]


# 딕셔너리(dict)
# key-value 쌍으로 구성된 매핑 자료형
# key는 불변 데이터 타입(일반적으로 문자열이나 숫자)이어야 하고,
# value는 어떤 데이터 타입도 가능하다.

empty_dict = {}
person_a = {"name": "Kim", "age": 20, "job": "student"}
number_a = {"one": 1, "two": 2, "three": 3}
person_b = dict(name="Kim", age=20, job="student")
number_b = dict(one=1, two=2, three=3)


# 집합(set)
# 중복된 값을 허용하지 않고, 순서가 없는 자료형
fruits = {"apple", "banana", "cherry", "apple", "cherry"}
print(fruits)            # {'apple', 'banana', 'cherry'}

empty_set = set()

number1 = {1, 2, 3, 4, 5}
number2 = set([4, 5, 6, 7, 8]) # 리스트를 set으로 변환

print(number1 & number2)    # 교집합    {4, 5}
print(number1 | number2)    # 합집합    {1, 2, 3, 4, 5, 6, 7, 8}
print(number1 - number2)    # 차집합    {1, 2, 3}


# 프로즌셋(frozenset)
# 불변 집합

empty_frozenSet = frozenset()
numbers = frozenset({1, 2, 3, 4, 5})  # set을 frozenset으로 변환, 값 수정 시 error 발생


# NoneType
# None을 가지는 데이터 타입
# None은 아무것도 없다는 것을 의미
# 모든 None 값은 동일한 객체를 참조

a = None
b = None
print(a == b) # True (값 비교)
print(a is b) # True (객체 비교)
print(type(a)) # <Class 'NoneType'>