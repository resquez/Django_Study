name = "Python"
age = 30
message = "Hello, {}! Your age is {}.".format(name, age)
print(message)

# 자리 표시자 내에 인덱스를 사용할 수 있습니다.
message = "Hello, {1}! Your age is {0}.".format(age, name)
print(message)

# 자리 표시자 내에 이름을 사용할 수 있습니다.
message = "Hello, {xname}! Your age is {xage}.".format(xname=name, xage=age)
print(message)

# 원주율을 소수점 둘째 자리까지 출력합니다.
pi = 3.14159256535
format_string = "원주율은 {:.2f}입니다.".format(pi)
print(format_string)

# 전체 자리수를 10으로 맞추고 왼쪽에 0으로 패딩합니다.
format_string = "원주율은 {:010.2f}입니다.".format(pi)
print(format_string)

# 문자열을 특정 너비에 맞추어 정렬합니다.
name = "HONG"
age = 23
address = "Seoul"
align_left = "|{:<10}|{:<10}|{:<10}|".format(name, age, address)
align_right = "|{:>10}|{:>10}|{:>10}|".format(name, age, address)
align_center = "|{:^10}|{:^10}|{:^10}|".format(name, age, address)
print(align_left)
print(align_right)
print(align_center)
