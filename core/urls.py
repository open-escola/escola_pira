from django.urls import path

from . import views, views_admin, views_staff, views_student

urlpatterns = [
    path('', views.go_login_page),
    path('index1/', views.go_index),
    path('index2/', views.go_index2),
    path('index3/', views.go_index3),
    path('get_user_detail', views.get_user_detail),

    path('login/', views.go_login_page, name='login'),
    path('forgot_password/', views.go_login_forgot, name='forgot-password'),
    path('recovery_password/', views.go_recovery, name='recovery-password'),
    path('register/', views.go_register, name='register'),
    path('do_login', views.do_login, name='do_login'),
    path('logout', views.do_logout, name='logout'),

    path('admin_home', views_admin.admin_home, name='admin_home'),

    path('add_staff', views_admin.add_staff, name='add_staff'),
    path('add_staff_save', views_admin.add_staff_save, name='add_staff_save'),

    path('add_course', views_admin.add_course, name='add_course'),
    path('add_course_save', views_admin.add_course_save, name='add_course_save'),

    path('add_student', views_admin.add_student, name='add_student'),
    path('add_student_save', views_admin.add_student_save, name='add_student_save'),

    path('add_subject', views_admin.add_subject, name='add_subject'),
    path('add_subject_save', views_admin.add_subject_save, name='add_subject_save'),

    path('manage_staff', views_admin.manage_staff, name='manage_staff'),
    path('manage_student', views_admin.manage_student, name='manage_student'),
    path('manage_course', views_admin.manage_course, name='manage_course'),
    path('manage_subject', views_admin.manage_subject, name='manage_subject'),

    path('edit_staff/<str:staff_id>', views_admin.edit_staff, name='edit_staff'),
    path('edit_staff_save', views_admin.edit_staff_save, name='edit_staff_save'),

    path('edit_student/<str:student_id>', views_admin.edit_student, name='edit_student'),
    path('edit_student_save', views_admin.edit_student_save, name='edit_student_save'),

    path('edit_subject/<str:subject_id>', views_admin.edit_subject, name='edit_subject'),
    path('edit_subject_save', views_admin.edit_subject_save, name='edit_subject_save'),

    path('edit_course/<str:course_id>', views_admin.edit_course, name='edit_course'),
    path('edit_course_save', views_admin.edit_course_save, name='edit_course_save'),

    path('manage_session', views_admin.manage_session, name='manage_session'),
    path('add_session_save', views_admin.add_session_save, name='add_session_save'),

    # Staff Aula 10
    path('staff_home', views_staff.staff_home, name='staff_home'),
    path('student_home', views_student.student_home, name='student_home'),

]
