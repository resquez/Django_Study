# 실습 7

num = 1
while num < 10:
    dan = 2
    while dan < 10:
        print(f'{dan} * {num} = {dan * num}', end='\t')
        dan+=1
    print()
    num+=1