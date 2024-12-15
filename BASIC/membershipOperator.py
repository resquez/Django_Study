# 리스트에 값이 포함되어 있는 지 확인하기
fruits = ['apple', 'banana', 'cherry']

if 'apple' in fruits:
    print('apple이 포함되어 있습니다.')

if 'grape' not in fruits:
    print('grape가 포함되어 있지 않습니다.')

# 문자열에 값이 포함되어 있는 지 여부를 확인
message = 'Hello, World!'
print('Hello'  in message)
print("hello" in message)

# 튜플에 값이 포함되어 있는 지 여부를 확인
members = ('James', 'Robert', 'Lisa', 'Mary')
print('Lisa'in members)
print('Lisa' not in members)


# 딕셔너리에 '키'를 포함하고 있는 지 여부를 확인
person = {"name": "John", "age": 36, "country": "Norway"}
print("name" in person)
print("John" in person)
print("gender" in person)