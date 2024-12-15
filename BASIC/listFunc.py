# 문자열을 리스트로 변환
str = "Hello"
lst = list(str)
print(lst)      # ['H', 'e', 'l', 'l', 'o']


# 튜플을 리스트로 변환
tpl = (10, 20, 30)
lst = list(tpl)
print(lst)      # [10, 20, 30]


lst.append(40)
tpl = tuple(lst)
print(tpl)      # (10, 20, 30, 40)


# 딕셔너리를 리스트로 변환 => 키값만 리스트로 반환
d = {'one':1, 'two':2, 'three':3}
lst = list(d)
print(lst)      # ['one', 'two', 'three']


# 집합을 리스트로 변환
s = {1, 2, 3}
lst = list(s)
print(lst)      # [1, 2, 3]