from django.urls import path, re_path, include
from . import views

urlpatterns = [
    #elections App의 views로 연결
    path('', views.index),
    path('candidate/', views.candidate),
    re_path('candidate/areas/(?P<area>.+)/$', views.areas),
    re_path('candidate/areas/(?P<area>.+)/results$', views.results),
    re_path('candidate/polls/(?P<poll_id>\d+)/$', views.polls),
]
    