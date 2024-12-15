# 파이썬 웹 프로그래밍
    - 목적 
        - (*)웹 서비스 구성
        - (*)향후 보안 처리시 대상이 되는 서비스 구현

    - 프레임웍(라이브러리, 패키지)
        - django
            - 무겁다, 대부분 필요한 구성요소가 만들어져 있다
            - spring/spring boot 와 유사한 포지션
        - (*)flask
            - 유연하다, 쉽다
            - node와 유사한 포지션
        - fastapi        
            - 가장 빠르다
            - 가장 최신에 나온 프레임웍

# 개발환경 구축
    - 파이썬 설치
    - 가상환경 구축(옵션, 대부분 필수임)
        - (secret_py)> ...
        - 없으면 파이썬에서 그대로 사용!!
    - 설치 패키지 구성
        - requirements.txt
        ``` 
            # 버전 생략 가능
            # 실제적으로는 버전관리 필요
            패키지[==버전]
            flask==1.0.2
        ```
    - 패키지 설치
        - (secret_py)현재디렉토리> pip install -r requirements.txt

# flask의 일반적 구조
    /
    L static        # 정적파일이 위치(이미지, css, js)
        L auth.js
        L logo.png
    L templates
        L login.html# html 파일
    L *.py          # 파이썬
    L db            # 응용해서 위치시킴
        L *.py

# 개발
    - (*)기본 골격
    - (*)데이터 전송
        - get
        - post
        - 동적 파라미터
    - (*)화면 랜더링
        - (*)SSR(Server Side Rendering) <-> CSR(Client Side Rendering)
        - 템플릿 엔진 : Jinja2
    - (*)데이터베이스 연동
        - flask <-> pymysql <-> mariadb
        - 자바진영 <-> 오라클
        - AWS <-> 오라클, mysql, 오로라,...
            - 표준 SQL 습득 => 제품별로 체크
            - mysql == 오로라 == mariadb =!= postgreSQL(KT)
            - 오라클 (전자정부)
            - MS계열(여행사, 항공, 숙박,..)- MS-SQL
            - .. <-> ORM을 이용하여 구성 
    - 이후
        - 개별주제
            - 로그인, 로그아웃, 회원가입 => 인증처리
                - 세션 로그인
                - JWT 로그인 -> 가장 많이 사용
                - oAUth 로그인 -> 메타, 구글, 네이버, 카카오, ..타 기업의 인증 사용
            - 게시판 -> CRUD 기능
            - 웹소켓 -> 실시간 네트워크 처리
            - LLM기반 AI 챗봇 -> 웹소켓, 템플릿처리, 외부통신, AI 응용(벡터디비 연동)
            - 검색 -> 엘라스틱서치(검색엔진)
            - ...

# 기본 골격
    - flask를 이용한 기본 웹서비스 뼈대 구성
        - f1