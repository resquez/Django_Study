from django.shortcuts import render, redirect
from django.db import connection
from .models import Board
from django.contrib import messages
from django.urls import reverse
from django.conf import settings

def board_write(request):
    # 로그인한 사용자가 접근했을 경우 허용
    if request.session.get('email'):
        # request가 POST일 경우 로직
        if request.method == "POST":
            r_title = request.POST.get('title')
            r_content = request.POST.get('content')
            r_file = request.FILES.get('file')  # 업로드된 파일 가져오기

            # 제목과 내용이 공백인지 체크
            if r_title.strip() != '' and r_content.strip() != '':
                try:
                    # 작성한 내용이 공백이 아닐 경우 DB에 값 입력
                    Board.objects.create(
                        title=r_title,
                        content=r_content,
                        email=request.session.get('email'),
                        file=r_file
                    )

                    # 성공적으로 값이 입력되었음을 사용자에게 알린다.
                    print("글 작성 완료")
                    messages.success(request, '게시글이 성공적으로 등록되었습니다.')
                    return redirect('board:board_list')
                except Exception as e:
                    # 데이터베이스 저장 실패 시
                    print(f"DB 저장 실패: {e}")
                    messages.error(request, '게시글 등록 중 오류가 발생했습니다.')
            else:
                # 제목과 내용이 공백일 경우
                print("공백으로 작성된 게시글")
                messages.error(request, '제목과 내용을 정확히 입력해 주세요.')
    else:
        # 로그인 사용자가 아닐 경우 처리
        print("로그인 필요")
        messages.error(request, '로그인 후 작성해 주세요.')
        return redirect('account:login')

    # POST가 아닌 경우 글 작성 페이지 렌더링
    return render(request, 'board/write.html')

def board_list(request):
    # GET 요청으로 전달된 검색어 받기
    query = request.GET.get('q', '').strip()

    # SQL 실행을 위한 cursor 등록
    cursor = connection.cursor()

    if query:
        # 검색어가 있을 경우 필터링된 SQL문 실행
        sql = f"""
            SELECT b_num, title, email, write_time 
            FROM board 
            WHERE d_check = true AND (title LIKE '%%{query}%%' OR content LIKE '%%{query}%%') 
            ORDER BY b_num DESC
        """
    else:
        # 검색어가 없을 경우 모든 게시글 반환
        sql = """
            SELECT b_num, title, email, write_time 
            FROM board 
            WHERE d_check = true 
            ORDER BY b_num DESC
        """
    
    cursor.execute(sql)
    boards = cursor.fetchall()

    # 템플릿 렌더링
    return render(request, 'board/list.html', {'boards': boards, 'query': query})

def board_view(request):
    if request.GET.get('b_num'):
        bNum = request.GET.get('b_num')

        # SQL 실행을 위한 cursor 등록
        cursor = connection.cursor()

        # 게시글 데이터 가져오기
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
                # 조회수 증가
                sql = f"UPDATE board SET v_num = v_num + 1 WHERE b_num = {bNum}"
                cursor.execute(sql)
                v_num += 1

            # 파일 경로 처리
            file_path = board[0][5]
            file_url = f"{settings.MEDIA_URL}{file_path}" if file_path else None
            file_name = file_path.split('/')[-1] if file_path else None

            # 댓글 작성 처리
            if request.method == "POST":
                create_comment(request, bNum)
                return redirect(f'/board/view?b_num={bNum}')

            # 댓글 목록 가져오기
            comments_sql = f"""
                SELECT id, content, email, created_at
                FROM board_comment
                WHERE board_id = {bNum}
                ORDER BY created_at ASC
            """
            cursor.execute(comments_sql)
            comments = cursor.fetchall()

            # 댓글 개수 가져오기
            comment_count_sql = f"""
                SELECT COUNT(*)
                FROM board_comment
                WHERE board_id = {bNum}
            """
            cursor.execute(comment_count_sql)
            comment_count = cursor.fetchone()[0]

            # 데이터 저장
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
                'comment_count': comment_count,  # 댓글 개수 전달
            }
        else:
            print("존재하지 않는 글")
            messages.error(request, '존재하지 않는 글 입니다.')
            return redirect('board:board_list')
    else:
        print("파라미터 값(b_num)이 없음")
        messages.error(request, '잘못된 접근 입니다.')
        return redirect('board:board_list')

    return render(request, 'board/view.html', content)

def board_update(request):
    # POST 요청 처리 로직
    if request.method == "POST":
        bNum = request.POST.get('b_num')
        print(f'{bNum} post')
        content = request.POST.get('content')
        r_file = request.FILES.get('file')  # 업로드된 파일 가져오기

        # 데이터가 공백인지 체크
        if content and content.strip() != '':
            try:
                cursor = connection.cursor()  # SQL 실행을 위해 커서 등록
                if r_file:
                    # 파일이 존재하는 경우 쿼리
                    sql = f"""
                        UPDATE board 
                        SET content = '{content}', file = '{r_file.name}' 
                        WHERE b_num = {bNum}
                    """
                else:
                    # 파일이 없는 경우 쿼리
                    sql = f"""
                        UPDATE board 
                        SET content = '{content}' 
                        WHERE b_num = {bNum}
                    """
                cursor.execute(sql)
                print("글 수정 완료")
                messages.success(request, '게시글이 성공적으로 수정되었습니다.')
                return redirect(f"{reverse('board:board_view')}?b_num={bNum}")
            except Exception as e:
                print(f"DB 수정 오류: {e}")
                messages.error(request, '게시글 수정 중 오류가 발생했습니다.')
        else:
            print("글 수정 실패: 공백 입력")
            messages.error(request, '내용을 정확히 입력해 주세요.')
            return redirect(f"{reverse('board:board_view')}?b_num={bNum}")

    # GET 요청 처리 로직
    elif request.method == "GET" and request.GET.get('b_num'):
        bNum = request.GET.get('b_num')
        print(f'{bNum} get')
        cursor = connection.cursor()
        sql = f'select email, title, content from board where b_num = {bNum} and d_check=true'
        cursor.execute(sql)
        board = cursor.fetchall()

        # 데이터가 존재하는지 체크
        if len(board) != 0:
            # 게시글 작성자 확인
            post_owner = board[0][0]
            if post_owner != request.session.get('email'):
                print("수정 권한 없음")
                messages.error(request, '게시글을 수정할 권한이 없습니다.')
                return redirect('board:board_list')

            # 수정 페이지 렌더링을 위한 데이터 저장
            content = {
                'title': board[0][1],
                'content': board[0][2],
                'b_num': bNum
            }
        else:
            # 글이 존재하지 않을 때
            print("존재하지 않는 글")
            messages.error(request, '존재하지 않는 글 입니다.')
            return redirect('board:board_list')

        # 수정 페이지 렌더링
        return render(request, 'board/update.html', content)

    # 잘못된 접근
    print("잘못된 접근: GET 또는 POST 요청이 아님")
    messages.error(request, '잘못된 접근입니다.')
    return redirect('board:board_list')

def board_delete(request):
    # 파라미터 값이 공백인지 체크
    if request.GET.get('b_num'):
        # 파라미터 값 변수에 저장
        bNum = request.GET.get('b_num')
        # SQL문을 실행하기 위해 cursor 등록
        cursor = connection.cursor()
        # SQL문 작성(존재하는 글의 email값을 받아옴)
        sql = f'select email from board where b_num = {bNum} and d_check=true'
        # 쿼리문 실행
        cursor.execute(sql)
        # 2차원 배열 형식으로 데이터 저장
        user = cursor.fetchall()

        # bNum의 글이 존재하는지 체크
        if len(user) != 0:
            # 존재할 경우 데이터 가공 -> 2차원 튜플 -> string
            user = user[0][0]
            # 삭제하는 사용자가 작성자 본인이 맞는지 체크
            if user == request.session.get('email'):
                # 작성자가 맞다면 삭제하는 SQL 작성
                sql = f'update board set d_check = false where b_num = {bNum}'
                # 쿼리문 실행
                cursor.execute(sql)
                # 삭제 성공
                print("글 삭제 완료")
                messages.success(request, '게시글이 성공적으로 삭제되었습니다.')
                return redirect('board:board_list')
            else:
                # 작성자가 아닐 시
                print("글 삭제 권한 없음")
                messages.error(request, '게시글을 삭제할 권한이 없습니다.')
                return redirect('board:board_list')
        else:
            # 존재하지 않는 글이거나, 삭제된 글일 경우
            print("존재하지 않는 글")
            messages.error(request, '이미 삭제된 글이거나, 존재하지 않습니다.')
            return redirect('board:board_list')
    else:
        # 파라미터 값이 없을 때
        print("파라미터 값(b_num)이 없음")
        messages.error(request, '잘못된 접근 입니다.')
        return redirect('board:board_list')
    
def create_comment(request, board_id):
    # 이메일 세션 확인하여 비회원인 경우 댓글 작성 차단
    if not request.session.get('email'):
        messages.error(request, '로그인 후 댓글을 작성할 수 있습니다.')
        return redirect(f'/board/view?b_num={board_id}')

    cursor = connection.cursor()
    comment_content = request.POST.get('comment', '').strip()

    # 댓글 내용이 비어있는지 확인
    if comment_content:
        email = request.session.get('email')
        try:
            # 댓글 작성 쿼리 실행
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

def delete_comment(request):
    if request.method == "POST":
        comment_id = request.GET.get('comment_id')  # 전역 고유 ID
        board_id = request.GET.get('b_num')  # 게시글 ID
        email = request.session.get('email')

        # 디버깅 로그
        print(f"comment_id: {comment_id}, board_id: {board_id}, email: {email}")

        if not comment_id or not board_id:
            messages.error(request, '댓글 ID나 게시글 ID가 제공되지 않았습니다.')
            return redirect('board:board_list')

        cursor = connection.cursor()

        # 댓글 가져오기
        sql = f"""
            SELECT email, board_id 
            FROM board_comment 
            WHERE id = {comment_id} AND board_id = {board_id} AND email = '{email}'
        """
        print(f"Executing SQL: {sql}")  # 실행된 SQL 확인
        cursor.execute(sql)
        comment = cursor.fetchone()

        if not comment:
            messages.error(request, '존재하지 않는 댓글이거나 삭제 권한이 없습니다.')
            return redirect('board:board_list')

        # 댓글 삭제
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

def update_comment(request):
    if request.method == "POST":
        comment_id = request.POST.get('comment_id')  # 댓글 ID
        board_id = request.POST.get('b_num')  # 게시글 ID
        new_content = request.POST.get('comment', '').strip()
        email = request.session.get('email')

        print(f'{comment_id}, {board_id}')        

        if not comment_id or not board_id or not new_content:
            messages.error(request, '댓글을 수정할 수 없습니다.')
            return redirect(f'/board/view?b_num={board_id}')

        cursor = connection.cursor()

        # 댓글 작성자 확인
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

        # 댓글 업데이트
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
