# 실습: 주민등록번호를 이용한 성별과 만 나이 계산
'''
사용자가 이름과 주민등록번호를 입력하면 "이름(성별) 만OO세" 형식으로 출력하는 프로그램을 작성해 보세요. 

사용자에게 이름과 주민등록번호를 입력받습니다. 
주민등록번호의 7번째 자리의 숫자를 이용해 성별을 판단합니다. (1과 3은 남성, 2와 4는 여성)
주민등록번호의 첫 6자리와 7번째 자리 숫자를 이용해 생년월일을 추출합니다. 7번째 자리 숫자가 1이나 2면 1900년대 출생, 3이나 4면 2000년대 출생으로 판단합니다.
datetime 모듈을 사용하여 현재 날짜와 생년월일을 비교하여 만 나이를 계산합니다. 
이름과 함께 성별, 만 나이를 출력합니다. 
'''

from datetime import datetime

def calculate_age(birthday):
    today = datetime.today()
    age = today.year - birthday.year
    if today.month < birthday.month or (today.month == birthday.month and today.day < birthday.day):
        age -= 1
    return age

def main():
    name = input("이름을 입력하세요: ")
    rrn = input("주민등록번호를 입력하세요 (예: 901010-1234567): ")
    
    # 주민등록번호에서 성별, 생년월일 추출
    # TODO
    
    # 성별 판별
    # TODO
    
    # 결과 출력
    print(f"{name}({gender}) 만{age}세")

if __name__ == "__main__":
    main()
