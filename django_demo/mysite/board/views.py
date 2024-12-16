from django.shortcuts import render, redirect
from django.db import connection
from .models import Board
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, Http404
from urllib.parse import unquote, urlencode
import os
import re


# 게시글 작성
def board_write(request):
    if request.session.get('email'):
        if request.method == "POST":
            r_title = request.POST.get('title')
            r_content = request.POST.get('content')
            r_file = request.FILES.get('file')  # 업로드된 파일 가져오기

            if r_title.strip() != '' and r_content.strip() != '':
                try:
                    if r_file:
                        file_name = r_file.name
                        upload_path = os.path.join(settings.MEDIA_ROOT, 'uploads')
                        os.makedirs(upload_path, exist_ok=True)
                        file_path = os.path.join(upload_path, file_name)

                        with open(file_path, 'wb+') as destination:
                            for chunk in r_file.chunks():
                                destination.write(chunk)

                        Board.objects.create(
                            title=r_title,
                            content=r_content,
                            email=request.session.get('email'),
                            file=file_name
                        )
                    else:
                        Board.objects.create(
                            title=r_title,
                            content=r_content,
                            email=request.session.get('email')
                        )

                    messages.success(request, '게시글이 성공적으로 등록되었습니다.')
                    return redirect('board:board_list')
                except Exception as e:
                    print(f"DB 저장 실패: {e}")
                    messages.error(request, '게시글 등록 중 오류가 발생했습니다.')
            else:
                messages.error(request, '제목과 내용을 정확히 입력해 주세요.')
    else:
        messages.error(request, '로그인 후 작성해 주세요.')
        return redirect('account:login')

    return render(request, 'board/write.html')


# 게시글 목록
def board_list(request):
    query = request.GET.get('q', '').strip()
    cursor = connection.cursor()

    if query:
        sql = f"""
            SELECT b_num, title, email, write_time 
            FROM board 
            WHERE d_check = true AND (title LIKE '%%{query}%%' OR content LIKE '%%{query}%%') 
            ORDER BY b_num DESC
        """
    else:
        sql = """
            SELECT b_num, title, email, write_time 
            FROM board 
            WHERE d_check = true 
            ORDER BY b_num DESC
        """
    
    cursor.execute(sql)
    boards = cursor.fetchall()

    paginator = Paginator(boards, 10)
    page = request.GET.get('page', 1)

    try:
        paginated_boards = paginator.page(page)
    except PageNotAnInteger:
        paginated_boards = paginator.page(1)
    except EmptyPage:
        paginated_boards = paginator.page(paginator.num_pages)

    return render(request, 'board/list.html', {
        'boards': paginated_boards,
        'query': query
    })


# 게시글 상세보기
def board_view(request):
    if request.GET.get('b_num'):
        bNum = request.GET.get('b_num')
        cursor = connection.cursor()
        sql = f"""
            SELECT title, email, content, v_num, write_time, file
            FROM board
            WHERE b_num = {bNum} AND d_check = true
        """
        cursor.execute(sql)
        board = cursor.fetchall()

        if len(board) != 0:
            v_num = board[0][3]
            if request.session.get('email') != board[0][1]:
                sql = f"UPDATE board SET v_num = v_num + 1 WHERE b_num = {bNum}"
                cursor.execute(sql)
                v_num += 1

            file_name = board[0][5].split('/')[-1] if board[0][5] else None
            file_url = reverse('board:file_download') + f"?{urlencode({'file': file_name})}" if file_name else None

            if request.method == "POST":
                create_comment(request, bNum)
                return redirect(f'/board/view?b_num={bNum}')

            comments_sql = f"""
                SELECT id, content, email, created_at
                FROM board_comment
                WHERE board_id = {bNum}
                ORDER BY created_at ASC
            """
            cursor.execute(comments_sql)
            comments = cursor.fetchall()

            comment_count_sql = f"""
                SELECT COUNT(*)
                FROM board_comment
                WHERE board_id = {bNum}
            """
            cursor.execute(comment_count_sql)
            comment_count = cursor.fetchone()[0]

            content = {
                'title': board[0][0],
                'email': board[0][1],
                'content': board[0][2],
                'v_num': v_num,
                'write_time': board[0][4],
                'file_url': file_url,
                'file_name': file_name,
                'b_num': bNum,
                'comments': comments,
                'comment_count': comment_count,
            }
        else:
            messages.error(request, '존재하지 않는 글 입니다.')
            return redirect('board:board_list')
    else:
        messages.error(request, '잘못된 접근 입니다.')
        return redirect('board:board_list')

    return render(request, 'board/view.html', content)


# 게시글 수정
def board_update(request):
    if request.method == "POST":
        bNum = request.POST.get('b_num')
        content = request.POST.get('content')
        r_file = request.FILES.get('file')  # 업로드된 파일 가져오기

        if content and content.strip() != '':
            try:
                cursor = connection.cursor()
                if r_file:
                    sql = f"""
                        UPDATE board 
                        SET content = '{content}', file = '{r_file.name}' 
                        WHERE b_num = {bNum}
                    """
                else:
                    sql = f"""
                        UPDATE board 
                        SET content = '{content}' 
                        WHERE b_num = {bNum}
                    """
                cursor.execute(sql)
                messages.success(request, '게시글이 성공적으로 수정되었습니다.')
                return redirect(f"{reverse('board:board_view')}?b_num={bNum}")
            except Exception as e:
                print(f"DB 수정 오류: {e}")
                messages.error(request, '게시글 수정 중 오류가 발생했습니다.')
        else:
            messages.error(request, '내용을 정확히 입력해 주세요.')
            return redirect(f"{reverse('board:board_view')}?b_num={bNum}")

    elif request.method == "GET" and request.GET.get('b_num'):
        bNum = request.GET.get('b_num')
        cursor = connection.cursor()
        sql = f'select email, title, content from board where b_num = {bNum} and d_check=true'
        cursor.execute(sql)
        board = cursor.fetchall()

        if len(board) != 0:
            post_owner = board[0][0]
            if post_owner != request.session.get('email'):
                messages.error(request, '게시글을 수정할 권한이 없습니다.')
                return redirect('board:board_list')

            content = {
                'title': board[0][1],
                'content': board[0][2],
                'b_num': bNum
            }
        else:
            messages.error(request, '존재하지 않는 글 입니다.')
            return redirect('board:board_list')

        return render(request, 'board/update.html', content)

    messages.error(request, '잘못된 접근입니다.')
    return redirect('board:board_list')


# 게시글 삭제
def board_delete(request):
    if request.GET.get('b_num'):
        bNum = request.GET.get('b_num')
        cursor = connection.cursor()
        sql = f'select email from board where b_num = {bNum} and d_check=true'
        cursor.execute(sql)
        user = cursor.fetchall()

        if len(user) != 0:
            user = user[0][0]
            if user == request.session.get('email'):
                sql = f'update board set d_check = false where b_num = {bNum}'
                cursor.execute(sql)
                messages.success(request, '게시글이 성공적으로 삭제되었습니다.')
                return redirect('board:board_list')
            else:
                messages.error(request, '게시글을 삭제할 권한이 없습니다.')
                return redirect('board:board_list')
        else:
            messages.error(request, '이미 삭제된 글이거나, 존재하지 않습니다.')
            return redirect('board:board_list')
    else:
        messages.error(request, '잘못된 접근 입니다.')
        return redirect('board:board_list')


# 댓글 작성
def create_comment(request, board_id):
    if not request.session.get('email'):
        messages.error(request, '로그인 후 댓글을 작성할 수 있습니다.')
        return redirect(f'/board/view?b_num={board_id}')

    cursor = connection.cursor()
    comment_content = request.POST.get('comment', '').strip()

    if comment_content:
        email = request.session.get('email')
        try:
            insert_comment_sql = f"""
                INSERT INTO board_comment (board_id, content, email, created_at)
                VALUES ({board_id}, '{comment_content}', '{email}', NOW())
            """
            cursor.execute(insert_comment_sql)
            messages.success(request, '댓글이 등록되었습니다.')
        except Exception as e:
            messages.error(request, '댓글 등록 중 오류가 발생했습니다.')
            print(f"댓글 등록 오류: {e}")
    else:
        messages.error(request, '댓글 내용을 입력해주세요.')

    return redirect(f'/board/view?b_num={board_id}')


# 댓글 삭제
def delete_comment(request):
    if request.method == "POST":
        comment_id = request.GET.get('comment_id')
        board_id = request.GET.get('b_num')
        email = request.session.get('email')

        if not comment_id or not board_id:
            messages.error(request, '댓글 ID나 게시글 ID가 제공되지 않았습니다.')
            return redirect('board:board_list')

        cursor = connection.cursor()
        sql = f"""
            SELECT email, board_id 
            FROM board_comment 
            WHERE id = {comment_id} AND board_id = {board_id} AND email = '{email}'
        """
        cursor.execute(sql)
        comment = cursor.fetchone()

        if not comment:
            messages.error(request, '존재하지 않는 댓글이거나 삭제 권한이 없습니다.')
            return redirect('board:board_list')

        try:
            delete_sql = f"DELETE FROM board_comment WHERE id = {comment_id} AND board_id = {board_id} AND email = '{email}'"
            cursor.execute(delete_sql)
            messages.success(request, '댓글이 성공적으로 삭제되었습니다.')
        except Exception as e:
            messages.error(request, '댓글 삭제 중 오류가 발생했습니다.')
            print(f"댓글 삭제 오류: {e}")

        return redirect(f'/board/view?b_num={board_id}')
    else:
        messages.error(request, '잘못된 요청입니다.')
        return redirect('board:board_list')


# 댓글 수정
def update_comment(request):
    if request.method == "POST":
        comment_id = request.POST.get('comment_id')
        board_id = request.POST.get('b_num')
        new_content = request.POST.get('comment', '').strip()
        email = request.session.get('email')

        if not comment_id or not board_id or not new_content:
            messages.error(request, '댓글을 수정할 수 없습니다.')
            return redirect(f'/board/view?b_num={board_id}')

        cursor = connection.cursor()
        sql_check = f"""
            SELECT email 
            FROM board_comment 
            WHERE id = {comment_id} AND board_id = {board_id}
        """
        cursor.execute(sql_check)
        comment = cursor.fetchone()

        if not comment or comment[0] != email:
            messages.error(request, '댓글 수정 권한이 없습니다.')
            return redirect(f'/board/view?b_num={board_id}')

        try:
            update_sql = f"""
                UPDATE board_comment
                SET content = '{new_content}', created_at = NOW()
                WHERE id = {comment_id} AND board_id = {board_id} AND email = '{email}'
            """
            cursor.execute(update_sql)
            messages.success(request, '댓글이 성공적으로 수정되었습니다.')
        except Exception as e:
            messages.error(request, '댓글 수정 중 오류가 발생했습니다.')
            print(f"댓글 수정 오류: {e}")

        return redirect(f'/board/view?b_num={board_id}')
    else:
        messages.error(request, '잘못된 요청입니다.')
        return redirect('board:board_list')


def download_file(request):
    file_name = request.GET.get('file')  # 파일 이름을 쿼리로 받음
    if not file_name:
        raise Http404("파일 이름이 제공되지 않았습니다.")  # 파일 이름이 없을 경우 404 반환

    # 파일 경로 생성
    file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', file_name)

    # 파일 존재 여부 확인
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
    else:
        raise Http404("파일이 존재하지 않습니다.")  # 파일이 없으면 404 반환