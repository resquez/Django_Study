'''
    - 1. 라우트 표현 추가 => URL을 추가
        - /users/login
    - 2. 동적 파라미터
        - 클라이언트의 입력 정보를 서버로 전송하는 방식
            - method
            - url에 데이터를 세팅해서 전송 => 동적 파라미터!!
                - 네이버 뉴스에서 많이 사용
                - 기사번호(예상)를 전송  
                - https://n.news.naver.com/mnews/article/029/0002910589
                    - 0002910589: 기사(뉴스) 번호
                    - 보안 상 문제 없는 데이터만 전송(보안 취약하기 때문)
        - 종류
            - get
            - post
            - put
            - ...
'''

from flask import Flask

app = Flask(__name__) 

@app.route('/')
def home():     
    return 'home' 

# ~/users/login
# http://127.0.0.1:5000/users/login
# 함수명은 동일 *.py 내부에서는 고유해야 한다!!
@app.route('/users/login')
def login():     
    return '로그인 페이지'       # 한글 정상 출력

# 동적 파라미터 예시, 문자열 전달
@app.route('/news/<news_id>')
def news(news_id):
    return f'전달된 데이터 {news_id}'

# 데이터/news/데이터, 데이터를 n개 이상 전달 가능한지?
@app.route('/<auth>/news2/<news_id>')
def news2(auth, news_id):
    return f'전달된 데이터 {auth} {news_id}'

# 타입 부여: int, float, path(flask에서만 나오는 형식)
# http://127.0.0.1:5000/news3/34535a => 404 not found
# http://127.0.0.1:5000/news3/34535 => 200 OK => 결과확인
@app.route('/news3/<int:news_id>')
def news3(news_id):
    return f'전달된 데이터 {news_id}'

# path
@app.route('/news4/<path:news_id>')
def news4(news_id):
    # URL 뒤에 있는 모든 /~ 값들도 모두 데이터로 간주
    return f'전달된 데이터 %s' % news_id.split('/')



if __name__=='__main__':
    app.run(debug=True)