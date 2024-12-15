numbers = [1, 2, 3, 4, 5]


# 1. 빈 리스트를 정의하고, 루프를 돌며 각 요소를 가공해서 리스트에 추가
new_numbers = []
for number in numbers:
    new_numbers.append(number ** 2)
print(new_numbers)

# 2. 리스트 컴프리헨션을 사용하여 한 줄로 작성
new_numbers = [ number ** 2 for number in numbers ]
print(new_numbers)

# 3. map() 함수를 사용하여 한 줄로 작성
def square(number):
    return number ** 2
new_numbers = map(square, numbers)
print(list(new_numbers))

# 4. map() 함수와 람다 표현식을 사용하여 한 줄로 작성
new_numbers = map(lambda number: number ** 2, numbers)
print(list(new_numbers))