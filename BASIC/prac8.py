# 실습 8

line = input('출력할 라인의 개수는? ')
line = int(line)

while line > 0:
    num = 0
    while num < line:
        print('*', end='')
        num+=1
    line-=1




line = input('출력할 라인의 개수는? ')
line = int(line)


x = 1
while line > 0:
    num = line - (line - x)
    x += 1
    line -= 1
    while num > 0:
        print('*', end='')
        num -= 1
    print()