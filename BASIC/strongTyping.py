# 강력한 타입 검사 예

x = "123" # 문자열
y = 456   # 정수

# TypeError: can only concatenate str (not "int") to str
# Print(x + y)
# 문자열이 와야 하는 자리에 정수가 와서 오류가 발생
# 문자열 결합 연산자

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(y + x)
# 숫자(정수)가 와야 하는 자리에 문자열이 와서 오류가 발생
# 덧셈 연산자

# 오류 해결 방안
# 필요로 하는 데이터 타입으로 명시적 변환

# str() 함수를 사용하여 정수를 문자열로 변환
print(x + str(y))

# int() 함수를 사용하여 문자열을 정수로 변환
print(int(x) + y)