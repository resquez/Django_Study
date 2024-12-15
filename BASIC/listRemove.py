# remove(value) : 리스트에서 첫번째로 일치하는 항목을 제거
fruits = ['apple', 'banana', 'cherry', 'banana', 'banana', 'grape']
fruits.remove('banana')        
print(fruits)                   # ['apple', 'cherry', 'banana', 'banana', 'grape']


# pop() : 리스트에서 마지막 항목을 제거하고 반환
popped_item = fruits.pop()      
print(fruits)                   # ['apple', 'cherry', 'banana', 'banana']
print(popped_item)              # grape


# pop(index) : 리스트에서 해당 인덱스의 항목을 제거하고 반환
popped_item = fruits.pop(1)    
print(fruits)                   # ['apple', 'banana', 'banana']
print(popped_item)              # cherry


# 슬라이싱을 이용해서 특정 범위의 항목을 제거
fruits = ['apple', 'banana', 'cherry', 'banana', 'banana', 'grape']
fruits[1:3] = []                # 1번 인덱스부터 3번 인덱스 전까지 제거
print(fruits)                   # ['apple', 'banana', 'banana', 'grape']


# del 키워드를 이용해서 특정 인덱스의 항목을 제거
fruits = ['apple', 'banana', 'cherry', 'banana', 'banana', 'grape']
del fruits[1]                    # 1번 인덱스 제거
print(fruits)                    # ['apple', 'cherry', 'banana', 'banana', 'grape']


# del 키워드와 슬라이싱을 이용해서 특정 범위의 항목을 제거
fruits = ['apple', 'banana', 'cherry', 'banana', 'banana', 'grape']
del fruits[1:3]                  # 1번 인덱스부터 3번 인덱스 전까지 제거
print(fruits)                    # ['apple', 'banana', 'banana', 'grape']