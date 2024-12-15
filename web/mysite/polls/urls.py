from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path("login_success/", views.login_success, name="login_success"),
]