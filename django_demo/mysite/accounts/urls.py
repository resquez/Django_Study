# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='home'),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("login2/", views.login2, name="login2"),
    path("logout/", views.logout, name="logout"),
    path("home/", views.home, name="home"),
    path('mypage/', views.mypage, name='mypage'),
    path('upload_profile_image/', views.upload_profile_image, name='upload_profile_image'),
    path('change_password/', views.change_password, name='change_password'),
]