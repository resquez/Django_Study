# 실습 3. 아래와 같은 형식으로 구구단을 출력하는 코드를 작성하시오.


for i in range(2, 10):
    for j in range(2, 10):
        print(f'{i}*{j}={i*j}')
    print()