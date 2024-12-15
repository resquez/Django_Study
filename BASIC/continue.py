
for i in range(3):
    print(i, end=' ')      # 0 1 2


print()


for i in range(3):
    if i == 1:
        break
    print(i, end=' ')      # 0


print()


for i in range(3):
    if i == 1:
        continue
    print(i, end=' ')      # 0 2


# 사용자가 입력한 내용에서 쉽표(,), 물음표(?), 느낌표(!)를 제외한 나머지 문자만 출력

user_input = input('메시지를 입력하세요: ')


for c in user_input:
    if c == ',' or c == '!' or c == '?':
        continue
   
    print(c, end='')
