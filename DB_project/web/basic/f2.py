'''
    - 코드 수정 시 자동인지 재가동 처리
      app.run(debug=True)
'''

from flask import Flask

app = Flask(__name__) 

@app.route('/')
def home():     
    # 코드 수정 -> 자동으로 인지 -> 서버 자동 재가동 -> 확인(개발시간 단축 가능)
    return 'hello flask3' 

if __name__=='__main__':
    # debug=True : 코드가 수정되면 자동 인식 후 재가동
    app.run(debug=True)