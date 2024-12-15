global_variable = "I am a global variable"

def my_funtion():
    # 전역 변수를 함수 내부에서 수정 가능하도록 설정
    global global_variable

    # 전역 변수의 값을 수정
    global_variable = "I am modifed global variable"
    print(global_variable)                   # I am modifed global variable
                                             # 수정된 지역 변수의 값을 출력


my_funtion()
print(global_variable)                       # I am modifed global variable
                                             # 함수 내부에서 수정된 전역 변수의 값을 출력