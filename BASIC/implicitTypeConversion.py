# 정수와 실수의 연산에서 암시적 형 변환
int_num = 10
float_num = 2.5

# int_num과 float_num을 더한 결과를 출력
# 정수와 실수가 혼합된 연산에서는 실수로 암시적 형 변환
result = int_num + float_num  # 10.0 + 2.5
print(result)
print(type(result))



# 블리언과 정수의 연산에서 암시적 형 변환
bool_value = True
int_value = 10

# 블리언 값이 정수로 변환
result = bool_value + int_value # 1 + 10
print(result)                   # 11


bool_value = False
int_value = 10

# 블리언 값이 정수로 변환
result = bool_value + int_value # 0 + 10
print(result)                   # 10

