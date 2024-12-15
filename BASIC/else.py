num = 9

if num > 20:
    print("20 보다 큰 수 입니다.")
elif num > 10:
    print("10 보다 크고 20 보다 작은 수 입니다.")
else:
    print("10 이하의 수 입니다.")

# 반복문에서 else 사용하기
for i in range(5):
    print(i, end='')
else:
    print("모두 출력되었습니다.")

for i in range(5):
    if i > 2:
        break
    print(i, end='')
else:
    print("모두 출력되었습니다.")