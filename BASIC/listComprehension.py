# 1부터 10까지의 숫자를 담은 리스트를 생성

# 1. 모든 항목을 직접 정의
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # >> 확장성 면에선 떨어짐


# 2. range를 정의
numbers = range(1, 11)
print(type(numbers))                      # <class 'range'>

numbers = list(numbers)
print(numbers)
print(type(numbers))                      # <class 'list'>

# 3. range의 값을 빈 리스트에 추가
numbers = []
for i in range(1, 11):
    numbers.append(i)

print(numbers)
print(type(numbers))

# List Comprehension
numbers = [i for i in range(1, 11)]

print(numbers)
print(type(numbers))

# 각 요소를 제곱해서 새로운 리스틀 생성
squared = [i**2 for i in range(1, 11)]
print(squared)              # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]