from django.urls import path, include
from . import views

urlpatterns = [
    #elections App의 views로 연결
    path('', views.index),
]
