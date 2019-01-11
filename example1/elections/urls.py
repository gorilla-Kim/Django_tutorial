from django.urls import path, re_path, include
from . import views

app_name = 'elections'

urlpatterns = [
    #elections App의 views로 연결
    path('', views.index, name = 'home'),
    path('candidate/', views.candidate),
    re_path('candidate/areas/(?P<area>.+)/$', views.areas),
    re_path('candidate/areas/(?P<area>.+)/results$', views.results),
    re_path('candidate/polls/(?P<poll_id>\d+)/$', views.polls),
    re_path('candidate/create/$', views.create_candidate, name = 'create_candidate'),
    re_path('poll/form$', views.form_poll, name = 'form_poll'),
    re_path('poll/create/$', views.create_poll, name = 'create_poll'),
    re_path('poll/show/$', views.show_poll, name = 'show_poll'),
]
    