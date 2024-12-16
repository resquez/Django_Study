# board/urls.py

from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('write/', views.board_write, name='board_write'),
    path('view/', views.board_view, name='board_view'),
    path('update/', views.board_update, name='board_update'),
    path('delete/', views.board_delete, name='board_delete'),
    path('download/', views.download_file, name='file_download'),
    path('create_comment/', views.create_comment, name='create_comment'),
    path('delete_comment/', views.delete_comment, name='delete_comment'),
    path('update_comment/', views.update_comment, name='update_comment'),
]