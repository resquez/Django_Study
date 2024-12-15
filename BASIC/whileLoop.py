# count가 5보다 작은 동안 count를 출력하고 1씩 증가시키는 코드
# 실행 결과: 0부터 4까지 출력

count = 0
while count < 5:
    print(count)
    count += 1


# 동일한 기능을 for문으로 표현
for count in range(5):
    print(count)