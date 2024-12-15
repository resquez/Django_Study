'''
    - 클라이언트가 서버로 데이터를 전송하는 방식
        - method -> post 방식
        - http 프로토콜의 body를 타고 전송(c -> s)
            - body의 사이즈가 크면 => 분활하여 전송(내부적으로 처리)
            - 전체 데이터가 수십 ~ 수백개로 쪼개저서 전송 
                - 순서에 대한 신뢰 필요 -> TCP/IP 기반 <-> UDP
            - ex)  
                - 대량의 파일 업로드
                - 보안에 유리 -> 실제는 암호화해 처리, https를 사용   
            - 약식 로그인             
'''
from flask import Flask, request, render_template, redirect
# 데이터베이스 모듈 가져오기
from db.d1 import login as login_process

app = Flask(__name__)

# 기본형태 -> GET 지원
# 브라우저 접속 => Method Not Allowed (405)=> 메소드 방식 추가하면됨
# @app.route('/', methods=['POST'])
@app.route('/')
def home():    
    return '홈페이지'

# 1. 로그인 페이지 -> get
# 2. 로그인 처리 ( 코드에서 처리, db 연동, 인증후처리x, 암호화x,.. )->post

# 1개의 url에서 메소드를 다르게 두어 여러 기능을 처리
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # 로그인 화면 담당
        # templates/index.html을 읽어서 랜더링해서(SSR, 서버측에서 페이지완성)
        # 클라이언트에게 전송
        return render_template('login.html')
    else:
        # 로그인 처리 담당 -> 최종적으로는 화면 x
        # 1. 사용자 아이디(이메일), 비번(암호화 x) 획득
        uid = request.form.get('uid')
        upw = request.form.get('upw')
        
        # 해당값이 둘다 존재할때!!
        if uid and upw:
            # 2. 정석 => DB 조회, JWT 처리등
            if login_process(uid, upw):
            # 2. 약식 => 고정값 문자열과 비교
            # 3. 약식-판단 
            #if uid == 'a@a.com' and upw == '1':            
                # 3-1. 성공 -> 세션생성 등등 :생략 -> 홈페이지이동
                return redirect('/') # 홈페이지 포워딩
            else:
                # 3-2. 실패 -> 경고창 띠움 -> 되돌아가기
                # 랜더링시 데이터를 전달핟고 싶다면 키=값
                #  msg="로그인정보확인"
                return render_template('alert.html', msg="로그인정보확인")
        else:
            # 경고창 => 이전화면으로 돌아가기
            return render_template('alert.html', msg="비정상접근")

if __name__== '__main__':
    app.run(debug=True)