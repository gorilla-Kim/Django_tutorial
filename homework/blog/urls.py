from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home_blog"),
    path('post/<int:pk>', views.post_view, name="post_view"),
    path('post/check/', views.pw_check, name="pw_check"),
    path('post/update/<int:pk>', views.post_update, name="post_update"),
    path('post/delete/<int:pk>', views.post_delete, name="post_delete"),
    path('post/create', views.post_create, name="post_create"),
]
