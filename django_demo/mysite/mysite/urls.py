from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls", namespace='main')),
    path('accounts/', include("accounts.urls", namespace='accounts')),
    path('board/', include('board.urls', namespace='board')),
]       

# 미디어 파일 서빙 설정 (개발 환경에서만)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)