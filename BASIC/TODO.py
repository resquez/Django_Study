# 숫자를 출력할 때 1000 단위로 콤마를 찍어서 오른쪽 정렬해서 출력하는 방법

number = 12345678901234567890234567890

print('%50s' % format(number, ','))

formatString = "{:,}".format(number)
print(formatString)

formatString = "{:>50,}".format(number)
print(formatString)