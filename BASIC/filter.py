numbers = [1, 2, 3, 4, 5]

evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)

print(evens)

evens = [ number for number in numbers if number % 2 == 0 ]
print(evens)

def is_even(number):
    return number % 2 == 0
evens = filter(is_even, numbers)
print(list(evens))

evens = filter(lambda number: number % 2 == 0, numbers)
print(list(evens))  # [2, 4]
