'''
    - 파이썬 데이터베이스 연동 예시
        - flask <-> pymysql <-> mariadb
    - 데이터베이스 연동 => I/O
'''
import pymysql as my

def login(uid, upw):
    # 1. 접속
    connection = my.connect(host    ='localhost',
                            user    ='root',
                            password='1234',
                            database='news',
                            cursorclass=my.cursors.DictCursor)
    
    # 반환값
    result = {}
    with connection:
        #print('데이터베이스 연결 성공')
        # 2. 커서오픈 -> 쿼리 -> 결과셋 획득
        with connection.cursor() as cursor:
            sql = '''
                SELECT *
                FROM user
                WHERE uid=%s AND upw=%s;
            '''
            # (sql, (인자1, 인자2, ...))
            # cursor.execute(sql, ('a@a.com','1234'))
            cursor.execute(sql, (uid, upw))  # 누구나 로그인 가능하게
            # 결과는 1개만 획득 -> 고객 정보 획득
            result = cursor.fetchone()
            #print('쿼리 결과', result)

        # 3. 연결닫기
        #print('데이터베이스 연결 종료')

    # 회원 정보 조회 결과 반환
    return result

# 모듈 개발자 테스트
if __name__ == '__main__':
    print('회원', login('a@a.com', '1234'))
    print('비회원', login('a@b.com', 'sdfas234'))