# count(value) : 리스트에 포함된 요소(value)의 개수를 반환
fruits = ['apple', 'banana', 'cherry', 'bnana', 'orange', 'banana' ]  
banana_count = fruits.count('banana')
print(banana_count)         # 3


# sort() : 리스트의 요소를 정렬
fruits = ['apple', 'banana', 'cherry', 'bnana', 'orange', 'banana' ]  
fruits.sort()
print(fruits)               # ['apple', 'banana', 'banana', 'bnana', 'cherry', 'orange']


# reverse() : 리스트의 요소를 역순으로 뒤집음
fruits = ['apple', 'banana', 'cherry', 'bnana', 'orange', 'banana' ]
fruits.reverse()            # fruits[::-1]과 동일
print(fruits)               # ['banana', 'orange', 'bnana', 'cherry', 'banana', 'apple']


# clear() : 리스트의 모든 요소를 제거  
fruits = ['apple', 'banana', 'cherry', 'bnana', 'orange', 'banana' ]
fruits.clear()
print(fruits)               # []