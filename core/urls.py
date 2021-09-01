from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_demo_page, name='home'),
    path('login/', views.show_login_page, name='login'),  # Vai pra página do Login
    path('do_login', views.do_login),
    path('get_user_detail', views.get_user_detail),
    path('logout_user', views.logout_user),
]
