# 실습 4: 가로로 구구단 출력

for i in range(1, 10):
    for j in range(2, 10):
        print(f"{j} * {i} = {i * j}", end='\t')
    print()