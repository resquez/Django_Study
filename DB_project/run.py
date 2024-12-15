# -*- coding: utf-8 -*-
'''
  - 데이터베이스 생성
    - CLI 모드
      - mariadb client ...
      - 비번입력
      - 데이터베이스 생성
        > create database news;
      - 데이터베이스 조회
        > show databases;
    - GUI 모드
    - 가상 환경 구성
      - 현 프로젝트상에서 구성
      - python -m venv secret_py
      - vscode 재가동
      - 코드 오픈 후 터미널 오픈(command prompt로 오픈)
        > (secret_py) C:\python\DB_project>pip list
      - 가상환경에 필요한 패키지 설치
        > pip install -q pandas pymysql sqlalchemy
      
      > python run.py
'''

# 리뷰시간, 복습시간 => 코드 리팩토링 수행 및 정리
# 개선사항 -> 함수화

import urllib
import urllib.request as req
import json
import html
import re
import pandas as pd
from sqlalchemy import create_engine

# pip install -q pandas
# pip install -q pymysql sqlalchemy

# 키 지정
NAVER_CLIENT_ID  = 'Yjal33Q4Dr8CRHSRzRqo'
NAVER_SECRET_KEY = 'YzIfSLB_YC'

# 2. 요청 URL
url = 'https://openapi.naver.com/v1/search/news.json'

# 람다 함수로 표현
cusUrlEncode = lambda kw:urllib.parse.quote( kw )

def make_url( url, kw, dp=10, pno=1, sort='sim' ):
  # 기본형 구현후 => 확장성 고려(다른 매개변수가 변경된다면?) => 함수 업그레이드 햇음
  return f'{url}?query={kw}&display={dp}&start={pno}&sort={sort}'


"""#### 통신모듈 함수화"""
def naver_search( url:str, kw:str, dp:int=10, pno:int=1, sort:str='sim' )->dict:
  '''
    네이버 검색 API를 이용하여 데이터를 추출하는 함수
    Parameters:
       ...
    Returns:
       ...
  '''
  final_url = make_url( url, cusUrlEncode(kw), dp, pno, sort )
  request   = req.Request( final_url )

  # 아이디와 키 세팅 부분 조정
  request.add_header( 'X-Naver-Client-Id', NAVER_CLIENT_ID )
  request.add_header( 'X-Naver-Client-Secret', NAVER_SECRET_KEY )

  try:
    response = req.urlopen( request ) # I/O -> 예외처리
    if response.getcode() == 200:
      # 만약, 응답 데이터에서 인코딩 오류가 발생한다면 => 인코딩 처리 후 반환
      return json.load( response )
    else:
      print( '통신 오류' )
      return {}
  except Exception as e:
    print( e )
    return {}

"""####  파싱모듈 함수화"""

# 정규식 패턴(html 태그 체크)
pattern = re.compile('<[a-zA-Z0-9]>|</[a-zA-Z0-9]>')
# 데이터별 클린 함수
data_clean = lambda x: pattern.sub('', html.unescape(x))

def data_preprocessing( datas ):
  results = list()

  for news in datas:
    # 원래 뉴스 데이터 -> 전처리 -> 다시 세팅
    # 필요한 데이터만 세팅, 이름 조정
    results.append({
        'title': data_clean( news['title'] ),
        'desc': data_clean( news['description'] ),
        'pubDate': data_clean( news['pubDate'] )
    })

  return results

# 조치2 -> 통신오류 나는 경우, 아래코드 추가
#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context

result     = naver_search(url, '트럼프')
clean_data = data_preprocessing( result['items'] ) #, type(result['items'])

# pandas 설치
# 딕셔너리 데이터로부터 데이터 프레임 생성
df = pd.DataFrame.from_dict( clean_data )

# 패키지 설치

# 데이터 베이스 적재

# 1. 모듈 가져오기
# import pymysql

# 2. 데이터베이스 접속 정보 준비
DB_HOST = '127.0.0.1' # 혹은 localhost, 실도메인(IP)
DB_ID = 'root'        # admin 계정이라 실제는 별도 계정 사용 권장
DB_PW = '1234'        # admin 계정의 비밀번호
DB_NAME = 'news'      # 사용할 데이터베이스 이름
DB_PORT = 3306        # mysql, mariadb, 오로라디비(AWS mysql 엔터급)
TABLE_NAME = 'news_tbl' # 데이터베이스상 테이블명
PROTOCOL = 'mysql+pymysql' # 데이터베이스 프로토콜 ex) http, ftp, ...

# 3. 접속 -> I/O: 예외처리, with문
# 3-1. 접속 URL 준비
db_url = f'{PROTOCOL}://{DB_ID}:{DB_PW}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
db_url

# 4. 데이터 밀어넣기

# 5. 연결 종료

# 작성만 하고 실제 수행은 로컬PC에서 *.py로 실행


# 3-2. 엔진 생성
engine = create_engine( db_url )

# 3-3. 접속(실제 연결)
conn = engine.connect()

# 4. 데이터 밀어넣기
df.to_sql( name=TABLE_NAME,          # 테이블명
          con=conn,                  # 접속객체
          if_exists='append',        # 추가(기존 데이터 유지), ... 지우고 다시 셋팅, ...
          index=False                # df에서 인덱스 파트는 데이터로 입력 X
          )

# 5. 연결 종료
conn.close()



"""#### 파이썬 덤프

- vscode 사용
- *.py

#### 자동화

- (*)윈도우 : 작업스케줄러
  - 하단 검색 > 스케 > 작업스케줄러 클릭
  - 우측 작업 만들기 클릭 > 새 작업 만들기
  - 일반
    - 이름, 설명
  - 트리거: 작업동작시간 설정
    - 고급
      - 작업반복시간: 10분 단위
      - 무제한
    - 동작
      - 위의 트리거 스케줄에 맞춰서 파이썬 파일을 작동시키겠다
      - 재료 : 작업 디렉토리, 파이썬 파일명
      - 프로그램
        - python.exe|pythonw.exe => 가상환경에 존재하는 파일로 세팅
        - 가상환경 사용자 (절대경로 필요)
          - C:\python\DB_project\secret_py\Scripts\pythonw.exe
        - os에 설치된 python 사용자 (환경변수에 classpath가 잡혀있다면)
          - pythonw.exe
      - 구동 예시
        - python run.py
    - 인수추가
      - run.py

    - 시작위치: run.py가 존재하는 디렉토리
      - C:\python\DB_project



- 리눅스 : cron (참고)

"""

