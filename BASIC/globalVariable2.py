global_variable = "I am a global variable"

def my_funtion():
    # 전역 변수의 값을 변경(수정)하는 것이 아니고,
    # 함수 내부에 전역 변수의 이름과 동일한 지역 변수를 정의
    global_variable = "I am modifed global variable"
    print(global_variable)                   # I am modifed global variable
                                             # 지역 변수의 값을 출력


my_funtion()
print(global_variable)                       # I am a global variable
                                             # 전역 변수의 값을 출력