number_a = 1
number_b = number_a
print(number_a)     # 1
print(number_b)     # 1


number_b = 2
print(number_a)     # 1 <= number_a는 변하지 않음
print(number_b)     # 2


# 얕은 복사
original = [1, 2, 3, 4, 5]
copied = original
print(original)     # [1, 2, 3, 4, 5]
print(copied)       # [1, 2, 3, 4, 5]


copied[0] = 10
print(copied)       # [10, 2, 3, 4, 5]
print(original)     # [10, 2, 3, 4, 5] <= original도 변함


# 슬라이싱을 이용한 깊은 복사
original = [1, 2, 3, 4, 5]
copied = original[:]
print(original)     # [1, 2, 3, 4, 5]
print(copied)       # [1, 2, 3, 4, 5]


copied[0] = 10
print(copied)       # [10, 2, 3, 4, 5]
print(original)     # [1, 2, 3, 4, 5] <= original은 변하지 않음


# copy() 메서드를 이용한 깊은 복사
original = [1, 2, 3, 4, 5]
copied = original.copy()
print(original)     # [1, 2, 3, 4, 5]