# append() : 리스트의 끝에 요소를 추가
fruits = [ 'apple', 'banana', 'cherry' ]
fruits.append('orange')
print(fruits)       # ['apple', 'banana', 'cherry', 'orange']


# insert(index, value) : 리스트의 index 위치에 value를 삽입
fruits.insert(1, 'grape')
print(fruits)       # ['apple', 'grape', 'banana', 'cherry', 'orange']