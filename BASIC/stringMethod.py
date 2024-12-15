str = "Hello World"


# len() 함수 : 문자열 길이를 반환
print(len(str))             # 11


# str.lower() : 문자열(str)을 소문자로 변환
print(str.lower())          # hello world


# str.upper() : 문자열(str)을 대문자로 변환
print(str.upper())          # HELLO WORLD


# str.strip() : 문자열(str)의 양쪽 공백을 제거
str = "    Hello Python    "
print(str.strip())          # Hello Python


# str.replace(old, new) : 문자열(str)에서 old를 new로 변경
str = "Hello Python!"
print(str.replace("Python", "World"))    # Hello World!


# str.split(delimiter) : 문자열(str)을 delimiter로 분리
# delimeter가 생략되면 공백을 기준으로 분리
str = "Hello world with Python!"
print(str.split())          # ['Hello', 'world', 'with', 'Python!']


# str.count(substring) : 문자열(str)에서 substring의 개수를 반환
str = "Hello Python!"
print(str.count("o"))       # 2


# str.find(substring) : 문자열(str)에서 substring의 위치를 반환
str = "Hello Python!"
print(str.find("Python"))   # 6
print(str.find("Java"))     # -1    (찾는 문자열이 없을 경우 -1 반환)


# str.index(substring) : 문자열(str)에서 substring의 위치를 반환
# find()와 동일하지만 찾는 문자열이 없을 경우 ValueError 발생
print(str.index("Python"))  # 6
# print(str.index("Java"))  # ValueError: substring not found


# in 연산자를 이용해서 문자열 포함 여부를 판단
str = "Hello Python!"
print("Python" in str)      # True
print("Java" in str)        # False