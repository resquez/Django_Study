hello = "HELLO"
world = "WORLD"

# 문자열에서 + 연산자를 사용하여 두 문자열을 연결
print(hello + world)

# 여러 문자열을 특정 구분자와 함께 연결하려면 join() 메서드 사용
# 형식: 구분자.join(문자열리스트)

words = ["Hello", "World", "with", "Python"]
result = " ".join(words)
print(result)        # Hello World with Python

result = "*".join(words)
print(result)        # Hello*World*with*Python

# 문자열에 * 연산자를 사용하면 문자열을 반복하게 됨
hello = "Hello"
print(hello * 3)