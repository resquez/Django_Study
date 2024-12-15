# 정수형을 실수형으로 명시적 형변환
int_number = 10
float_number = float(int_number)


print(float_number)         # 10.0
print(type(float_number))   # <class 'float'>




# 실수형을 정수형으로 명시적 형변환
float_number = 10.5
int_number = int(float_number)


print(int_number)           # 10
print(type(int_number))     # <class 'int'>




# 문자열을 정수형으로 명시적 형변환
string_number = "10"
int_number = int(string_number)


print(string_number)        # 10
print(type(string_number))  # <class 'str'>


print(int_number)           # 10
print(type(int_number))     # <class 'int'>




# 정수형을 문자열로 명시적 형변환
int_number = 123
string_number = str(int_number)


print(int_number)           # 123
print(type(int_number))     # <class 'int'>


print(string_number)        # 123
print(type(string_number))  # <class 'str'>