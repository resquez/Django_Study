# 정수형
a = 10              # 양의 정수
b = -5              # 음의 정수
c = 1234567890      # 정수의 크기에 제한이 없음(메모리 크기만큼)


# 실수형(float)
a = 3.14
b = -0.001
c = 2.5e3           # 2.5 * 10^3 = 2500.0


# 블리언(bool)
a = True
b = False

# 문자열(str)
# 문자열 내부에는 시작/끝 문자열을 제외한 나머지 기호를 사용할수 있음
# 만약에 문자열 내부에서 시작/끝 문자열을 사용하고 싶다면, 이스케이프 문자(\)를 사용
a = 'Hello, world!'
a_escape = 'Hello, "MY" \'MY\' world!'
b = "Python Programming"

print(a)
print(a_escape)
print(b)

c = '''I'm
a
student.'''           # docstring
d = """Python
    is
    "Very" 'very'
    fun!"""           # docstring
print(c)
print(d)
