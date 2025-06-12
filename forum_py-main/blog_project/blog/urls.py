from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home, name='home'),
    path('post/',views.post_list,name='post_list'),
    path('post/<int:post_id>', views.post_detail,name='post_detail'),
    path('post/new/', views.create_post, name='create_post'),
    path('upload_avatar/', views.upload_avatar, name='upload_avatar'),
    path('profile/<int:user_id>', views.profile_view, name='profile'),
]
