def my_function():
    local_variable = "I am a local variable"
    print(local_variable)                      # 함수 내에서 지역 변수에 접근이 가능

my_function()
#print(local_variable)                          # 함수 박에서는 함수 내부의 지역 변수에 접근할 수 없음
                                               # NameError: name 'local_variable' is not defined