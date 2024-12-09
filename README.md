
# [Django_Study 저장소](https://github.com/resquez/Django_Study)

## Django 데모 프로젝트

이 저장소는 Django를 활용한 웹 애플리케이션 개발 학습을 위한 데모 프로젝트입니다.

---

## 프로젝트 구조

```
django_demo/
├── manage.py
├── django_demo/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── app/
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py
```

- **django_demo/**: 메인 프로젝트 디렉토리로, 설정 파일과 URL 라우팅을 포함합니다.
- **app/**: 주요 애플리케이션 로직이 위치한 디렉토리로, 모델, 뷰, 관리자 설정 등이 포함됩니다.

---

## 시작하기

1. **저장소 클론**:

   ```bash
   git clone https://github.com/resquez/Django_Study.git
   cd Django_Study/django_demo
   ```

2. **가상 환경 설정**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Unix/macOS
   venv\Scripts\activate     # Windows
   ```

3. **필수 패키지 설치**:

   ```bash
   pip install -r requirements.txt
   ```

4. **마이그레이션 적용 및 슈퍼유저 생성**:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **개발 서버 실행**:

   ```bash
   python manage.py runserver
   ```

브라우저에서 `http://127.0.0.1:8000/`에 접속하여 애플리케이션을 확인할 수 있습니다.

---

## 기능

- **사용자 인증**: Django의 기본 인증 시스템을 활용한 로그인 및 로그아웃 기능
- **게시판**: CRUD 기능을 갖춘 게시판 모듈
  
---

## 참고 자료

- [Django 공식 문서](https://docs.djangoproject.com/ko/4.0/)
- [Python 공식 웹사이트](https://www.python.org/)
