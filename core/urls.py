from django.urls import path

from . import views, views_admin

urlpatterns = [
    path('', views.go_login_page),
    path('index1/', views.go_index),
    path('index2/', views.go_index2),
    path('index3/', views.go_index3),

    path('login/', views.go_login_page, name='login'),
    path('forgot_password/', views.go_login_forgot, name='forgot-password'),
    path('recovery_password/', views.go_recovery, name='recovery-password'),
    path('register/', views.go_register, name='register'),

    path('do_login', views.do_login),
    path('logout', views.do_logout),
    path('get_user_detail', views.get_user_detail),

    path('admin_home', views_admin.admin_home),

    path('add_staff', views_admin.add_staff),
    path('add_staff_save', views_admin.add_staff_save),

    path('add_course', views_admin.add_course),
    path('add_course_save', views_admin.add_course_save),

    path('add_student', views_admin.add_student),
    path('add_student_save', views_admin.add_student_save),

    path('add_subject', views_admin.add_subject),
    path('add_subject_save', views_admin.add_subject_save),

    path('manage_staff', views_admin.manage_staff),
    path('manage_student', views_admin.manage_student),
    path('manage_course', views_admin.manage_course),
    path('manage_subject', views_admin.manage_subject),

    path('edit_staff/<str:staff_id>', views_admin.edit_staff),
    path('edit_staff_save', views_admin.edit_staff_save),

    path('edit_student/<str:student_id>', views_admin.edit_student),
    path('edit_student_save', views_admin.edit_student_save),

]
