def my_func(): # 함수 선언부(헤더, 시그니처) => def 함수이름(매개변수):
    pass       # 함수 구현부(본문) => pass는 아무것도 하지 않는다는 의미 

class MyClass: # 클래스 선언
    pass       # 클래스 구현부


for i in range(5):
    if i == 3:
        pass
    else:
        print(i)



# 위에 코드는 아래와 같은 의미
for i in range(5):
    if i != 3:
        print(i)

 
for i in range(5):
    if i == 3:
        continue
    print(i)
