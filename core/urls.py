from django.urls import path
from . import views

urlpatterns = [
    path('', views.go_index),
    path('index1/', views.go_index),
    path('index2/', views.go_index2),
    path('index3/', views.go_index3),

    path('login/', views.go_login_page, name='login'),
    path('forgot-password/', views.go_login_forgot, name='forgot-password'),
    path('recovery-password/', views.go_recovery, name='recovery-password'),
    path('register/', views.go_register, name='register'),

    path('do_login', views.do_login),
    path('logout_user', views.do_logout_user),
    path('get_user_detail', views.get_user_detail),
]
