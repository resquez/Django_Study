# 실습 1. 중복 문자 제거
# 사용자가 입력한 문자열에서 중복된 문자를 제거하고 반환하는 remove_duplicate_chars 함수를 작성해 보세요. 

def remove_duplicate_chars(s):
    print(type(s))
    print(s)
    s = set(s)                      # 문자열을 set으로 변환 ==> 중복이 제거 됨
    print(type(s))
    print(s)
    s = ''.join(s)                  # set을 다시 문자열로 변환
    print(type(s))
    print(s)
    return s


str = input('문자열을 입력하세요 : ')
rdc = remove_duplicate_chars(str)

print(f'원문: [{str}] >>> {len(str)}글자')
print(f'중복제거: [{rdc}] >>> {len(rdc)}글자')