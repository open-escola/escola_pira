from django.urls import path
from . import views, views_admin


urlpatterns = [
    path('', views.go_login_page),
    path('index1/', views.go_index),
    path('index2/', views.go_index2),
    path('index3/', views.go_index3),

    path('login/', views.go_login_page, name='login'),
    path('forgot-password/', views.go_login_forgot, name='forgot-password'),
    path('recovery-password/', views.go_recovery, name='recovery-password'),
    path('register/', views.go_register, name='register'),

    path('do_login', views.do_login),
    path('logout_user', views.do_logout),
    path('get_user_detail', views.get_user_detail),


    path('admin_home', views_admin.admin_home),
    path('add_staff', views_admin.add_staff),
    path('add_staff_save', views_admin.add_staff_save),
]
