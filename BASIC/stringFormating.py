name = "홍길동"
age = 24
weight = 65.5

# 위의 데이터(프로파일)를 아래와 같은 형식으로 출력
# 이름 [홍길동]
# 나이 [24]
# 몸무게 [65.5]

profile = "이름 [%s]\n나이 [%d]\n몸무게 [%.1f]" % (name, age, weight)
print(profile)


# 너비를 지정
profile = "이름 [%10s]\n나이 [%10d]\n몸무게 [%10.1f]" % (name, age, weight)
print(profile)


# 왼쪽 정렬
profile = "이름 [%-10s]\n나이 [%-10d]\n몸무게 [%-10.1f]" % (name, age, weight)
print(profile)

# 공백을 0으로 채우기
profile = "이름 [%010s]\n나이 [%010d]\n몸무게 [%010.1f]" % (name, age, weight)
print(profile)