from django.shortcuts import render, redirect
from django.db import connection
from .models import CustomUser, Login_Check, Login_Check2
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse, Http404
from urllib.parse import unquote, urlencode
import os
import re

def home(request):
    users = CustomUser.objects.all()
    context = {'users': users}
    return render(request, 'accounts/home.html', context)

def register(request):
    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if email.strip() and name.strip() and password1.strip() and password2.strip():
            if password1 == password2: 
            # CustomUser 인스턴스 생성
                try:
                    CustomUser.objects.create_user(
                        username=email,
                        email=email,  
                        name=name,  
                        password=password1
                    )
                    return redirect('main:main')
                except Exception as e:
                    print(f"예외 발생: {e}")
                    if(e.args[0]==1062):
                        messages.error(request, '이메일 중복.')
                        return redirect('accounts:register')
                    else:
                        messages.error(request, '예기치 못한 오류가 발생했습니다. 다시 시도해주세요.')
                        return redirect('accounts:register')
            else:
                messages.error(request, '비밀번호가 일치하지 않습니다.')
                return redirect('accounts:register')
        else:
            messages.error(request, '빈칸을 확인해주세요.')
            return redirect('accounts:register')
        
    return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        login_data = {
            'email': email,
            'password': password
        }
        user_data = Login_Check(**login_data)

        if user_data is not None:
            try:
                user_email, user_password, user_name, user_profile_image = user_data

                # 세션 저장
                request.session['email'] = user_email
                request.session['name'] = user_name

                # 프로필 이미지 경로 설정
                if user_profile_image:
                    file_name = os.path.basename(user_profile_image)
                    request.session['profile_image'] = f"/accounts/download?file={file_name}"
                else:
                    request.session['profile_image'] = "https://via.placeholder.com/120"

                messages.success(request, '로그인 성공!')
                return redirect('main:main')
            except Exception as e:
                print(f"로그인 중 오류 발생: {e}")
                messages.error(request, '예기치 못한 오류가 발생했습니다.')
        else:
            messages.error(request, '이메일 또는 비밀번호가 일치하지 않습니다.')

    return render(request, 'accounts/login.html')


def login2(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        login_data = {
            'email': email,
            'password': password
        }
        user_data = Login_Check2(**login_data)

        if user_data is not None and user_data[1] == password:
            try:
                user_email, user_password, user_name, user_profile_image = user_data

                # 세션 저장
                request.session['email'] = user_email
                request.session['name'] = user_name

                # 프로필 이미지 경로 설정
                if user_profile_image:
                    file_name = os.path.basename(user_profile_image)
                    request.session['profile_image'] = f"/accounts/download?file={file_name}"
                else:
                    request.session['profile_image'] = "https://via.placeholder.com/120"

                messages.success(request, '로그인 성공!')
                return redirect('main:main')
            except Exception as e:
                print(f"로그인2 중 오류 발생: {e}")
                messages.error(request, '예기치 못한 오류가 발생했습니다.')
        else:
            messages.error(request, '이메일 또는 비밀번호가 일치하지 않습니다.')

    return render(request, 'accounts/login2.html')

def logout(request):
    if 'email' in request.session:
        del request.session['email']
        del request.session['name']
        del request.session['profile_image']
        return redirect('main:main')
    
# 마이페이지
def mypage(request):
    if not request.session.get('email'):
        messages.error(request, '로그인이 필요합니다.')
        return redirect('accounts:login')

    return render(request, 'accounts/mypage.html', {
        'email': request.session.get('email'),
        'name': request.session.get('name'),
        'profile_image': request.session.get('profile_image', "https://via.placeholder.com/120"),
    })



# 프로필 이미지 업로드
def upload_profile_image(request):
    if not request.session.get('email'):
        messages.error(request, '로그인이 필요합니다.')
        return redirect('accounts:login')

    if request.method == "POST":
        profile_image = request.FILES.get("profile_image")
        if profile_image:
            try:
                # 프로필 이미지 저장 경로 생성
                upload_dir = os.path.join(settings.MEDIA_ROOT, 'profile_images')
                os.makedirs(upload_dir, exist_ok=True)

                # 파일명 생성
                file_name = f"{request.session.get('email')}_profile.{profile_image.name.split('.')[-1]}"
                file_path = os.path.join(upload_dir, file_name)

                # 기존 파일 삭제
                cursor = connection.cursor()
                email = request.session.get('email')
                cursor.execute(f"SELECT profile_image FROM users WHERE email = '{email}'")
                existing_image = cursor.fetchone()

                if existing_image and existing_image[0]:
                    existing_file_path = os.path.join(settings.MEDIA_ROOT, existing_image[0])
                    if os.path.exists(existing_file_path):
                        os.remove(existing_file_path)

                # 새 파일 저장
                with open(file_path, 'wb+') as destination:
                    for chunk in profile_image.chunks():
                        destination.write(chunk)

                # 세션 및 DB에 파일 경로 저장
                profile_image_url = f"profile_images/{file_name}"
                request.session['profile_image'] = f"/accounts/download?file={file_name}"

                cursor.execute(
                    f"UPDATE users SET profile_image = '{profile_image_url}' WHERE email = '{email}'"
                )
                messages.success(request, '프로필 이미지가 업데이트되었습니다.')
            except Exception as e:
                print(f"파일 업로드 중 오류 발생: {e}")
                messages.error(request, '파일 업로드 중 오류가 발생했습니다.')
        else:
            messages.error(request, '업로드할 파일을 선택하세요.')

    return redirect('accounts:mypage')


# 파일 다운로드
def download_file(request):
    file_name = request.GET.get('file')
    if not file_name:
        raise Http404("파일 이름이 제공되지 않았습니다.")

    # 파일 경로 설정
    file_path = os.path.join(settings.MEDIA_ROOT, 'profile_images', file_name)

    # 파일 응답 반환
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'
            return response
    else:
        raise Http404("파일이 존재하지 않습니다.")
    

def change_password(request):
    if not request.session.get('email'):
        messages.error(request, '로그인 후 접근 가능합니다.')
        return redirect('accounts:login')

    if request.method == 'POST':
        # 폼 데이터 가져오기
        old_password = request.POST.get('old_password', '').strip()
        new_password = request.POST.get('new_password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()
        email = request.session.get('email')  # 세션에서 사용자 이메일 가져오기

        # 비밀번호 유효성 확인
        if not old_password or not new_password or not confirm_password:
            messages.error(request, '모든 필드를 입력해주세요.')
            return redirect('accounts:change_password')

        if new_password != confirm_password:
            messages.error(request, '새 비밀번호와 확인 비밀번호가 일치하지 않습니다.')
            return redirect('accounts:change_password')

        cursor = connection.cursor()
        try:
            # 기존 비밀번호 검증
            check_sql = f"SELECT * FROM users WHERE email = '{email}' AND password = '{old_password}'"
            cursor.execute(check_sql)
            user = cursor.fetchone()

            if not user:
                messages.error(request, '현재 비밀번호가 일치하지 않습니다.')
                return redirect('accounts:change_password')

            # 새 비밀번호 업데이트 (Raw SQL 사용)
            update_sql = f"UPDATE users SET password = '{new_password}' WHERE email = '{email}'"
            cursor.execute(update_sql)
            messages.success(request, '비밀번호가 성공적으로 변경되었습니다.')
            return redirect('accounts:mypage')

        except Exception as e:
            print(f"Error during password update: {e}")
            messages.error(request, '비밀번호 변경 중 오류가 발생했습니다.')
            return redirect('accounts:change_password')

    return render(request, 'accounts/change_password.html')