global_variable = "I am a global variable"

def my_funtion():
    print(global_variable)                   #  함수 내부에서 전역 변수의 값을 사용 가능


my_funtion()
print(global_variable)                       #  함수 외부에서도 전역 변수의 값을 사용 가능