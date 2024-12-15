'''
    - flask 기본 뼈대
'''

# 1. 모듈 가져오기
from flask import Flask   # 플라스크 모듈에서 플라스크 객체를 가져온다


# 2. 앱생성(서버생성)
app = Flask(__name__)     # __name__ => "__main__" or "파일명"으로 해석 

# 3. 라우팅 -> 요청 URL을 해석 --> 어떤 함수가 처리할 지 판단 -> 관련 함수 호출
# 데코레이터를 통해서 URL, method(get, post, ...) 정의됨  --> 100군데에 똑같은 수행을 할 수 있어 코드가 심플해진다?
@app.route('/') # URL 
def home():                      # 함수콜 -> 요청
    # 문자열을 응답
    return 'hello flask'         # 응답



# 4. 서버가동
if __name__=='__main__': # 엔트리포인트 코드의 진입로, 시작점, 메인
    app.run()