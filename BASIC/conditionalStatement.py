age = input(('나이를 입력하세요: '))
age = int(age)

is_employed = input('직장인입니까? (y/n): ')
if is_employed == 'y' or is_employed == 'Y':
    is_employed = True
else:
    is_employed = False

if int(age) < 19:
    print('애들은 가라')

if int(age) >= 18:
    print('성인입니다.')
    if is_employed:
        print('성인이면서 직장인입니다.')
    else:
        print('성인인데 백수십니다.')
elif age >= 13:
    print('청소년입니다.')
else:
    print('어린이입니다.')

# 삼항연산자
message = '성년입니다.' if age >= 20 else '미성년자입니다.'
print(message)