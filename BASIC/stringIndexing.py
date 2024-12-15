# 문자열 인덱싱과 슬라이싱

#      0         1
#      01234567890123
str = "Hello, Python!"


# 인덱스를 이용해서 문자를 추출
print(str[0])       # H  
print(str[7])       # P
print(str[-1])      # !
print(str[-7])      # P


# 슬라이싱을 이용해서 문자열을 추출
# [start:end:step] 형식을 사용


print(str[0:5])     # Hello             # 0 <= index < 5
print(str[7:])      # Python!           # 7 <= index < 끝까지
print(str[:5])      # Hello             # 0 <= index < 5
print(str[:])       # Hello, Python!    # 0 <= index < 끝까지


print(str[::2])     # Hlo yhn           # 0 <= index < 끝까지, 2씩 증가
print(str[::-1])    # !nohtyP ,olleH    # 끝부터 처음까지, 1씩 감소 = 문자열을 역순으로 출력
print(str[1::2])    # el,Pto!           # 1 <= index < 끝까지, 2씩 증가


