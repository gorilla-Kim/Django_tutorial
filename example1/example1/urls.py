from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #elections App의 urls로 연결
    path('', include('elections.urls')),
    path('admin/', admin.site.urls),
]
