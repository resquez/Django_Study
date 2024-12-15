# 실습 5.

line = input('출력할 라인의 개수는? : ')
for num in range(int(line)):
    for x in range(num):
        print('*', end='')
    print()