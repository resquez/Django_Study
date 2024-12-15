numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]


new_numbers = []
for number in numbers:
    if number % 2 == 0:
        new_numbers.append(number ** 2)
print(new_numbers)          # [4, 16, 36, 64, 100]




new_numbers = [ number ** 2 for number in numbers if number % 2 == 0 ]
print(new_numbers)          # [4, 16, 36, 64, 100]




new_numbers = filter(lambda number: number % 2 == 0, numbers)
new_numbers = map(lambda number: number ** 2, new_numbers)
print(list(new_numbers))    # [4, 16, 36, 64, 100]


####################################################################


numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]


new_numbers = []
for number in numbers:
    if number % 2 == 0:
        new_numbers.append(number ** 2)
print(new_numbers)          # [4, 16, 36, 64, 100]




new_numbers = [ number ** 2 for number in numbers if number % 2 == 0 ]
print(new_numbers)          # [4, 16, 36, 64, 100]




new_numbers = filter(lambda number: number % 2 == 0, numbers)
new_numbers = map(lambda number: number ** 2, new_numbers)
print(list(new_numbers))    # [4, 16, 36, 64, 100]
