name = "python"
age = 30
print(f"Hello, {name}! You are {age} years old.")   # Hello, Python! You are 30 years old.

# 변수 뿐 아니라 표현식도 가능
print(f"Next year, your will be {age + 1} years old.") 

# 부동 소수점 수를 출력할 때 소수점 이하 자릿수를 제한할 수 있다.
pi = 3.141592
print(f"원주율 = {pi:.2f}")        # 원주율 = 3.14

# 정렬과 공백 채우기
print(f"{'hello':10}python")
print(f"{'hello':<10}python")
print(f"{'hello':>10}python")
print(f"{'hello':^10}python")

# 공백 채우기
print(f"{'hello':*<10}python")  # hello*****python
print(f"{'hello':*>10}python")  # *****hellopython
print(f"{'hello':*^10}python")  # **hello***python