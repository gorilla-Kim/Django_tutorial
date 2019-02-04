from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home_blog"),
    path('post/<int:pk>', views.post_view, name="post_view"),
]
