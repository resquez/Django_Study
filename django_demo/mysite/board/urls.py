# board/urls.py

from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
	path('', views.board_list, name='board_list'),
    path('view', views.board_view, name='board_view'),
    path('write', views.board_write, name='board_write'),
    path('update', views.board_update, name='board_update'),
    path('delete', views.board_delete, name='board_delete'),
    path('comment/delete/', views.delete_comment, name='delete_comment'),
    path('comment/update/', views.update_comment, name='update_comment'),
]