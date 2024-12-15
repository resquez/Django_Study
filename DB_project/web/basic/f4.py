'''
    - 클라이언트가 서버로  데이터를 전송하는 방식
        - method -> get 방식
        - url?키=값&키=값 ...
        - "http 프로토콜 헤더(고정사이즈)를 타고 데이터가 전달된다"
            - 크기 제한이 존재
            - 데이터의 크기가 작고, 보안에 취약한 특징
            - 노출되어도 문제는 없는 데이터만 전송
'''

from flask import Flask, request

app = Flask(__name__) 

@app.route('/')
def home():   
    # 클라이언트가 서버에게 특정 페이지를 요청(request)한다!! 
    # 클라이언트가 서버로 보낸 모든 데이터는 request 객체가 가지고 있다!!!

    # http://127.0.0.1:5000/?pno=10&did=123
    # get 방식으로 전달된 데이터 획득 시 -> request.args.get('키)
    page_no = request.args.get('pno')
    doc_id  = request.args.get('did')
    # 전달된 값이 없다면(안 보냈거나, 키 값이 오타) => None으로 반환
    return f'홈페이지 {page_no} / {doc_id}'

if __name__=='__main__':
    app.run(debug=True)