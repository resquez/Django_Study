# numbers 리스트에서 짝수만 추출해서 even_numbers 이름의 리스트에 담아 출력하기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [ ]
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)


# list comprehension
even_numbers = [ number for number in numbers if number % 2 == 0 ]
print(even_numbers)

# 짝수를 거듭제곱해서 새로운 리스트 생성
even_numbers_squared = [ number ** 2 for number in numbers if number % 2 == 0 ]
print(even_numbers_squared)