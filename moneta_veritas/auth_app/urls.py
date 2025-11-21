from django.urls import path
from . import views

app_name = 'auth_app'

urlpatterns = [
    path('check-user/', views.check_user_exists, name='check_user_exists'),
    path('login/', views.login_user, name='login_user'),
    path('register/', views.register_user, name='register_user'),
    path('logout/', views.logout_user, name='logout_user'),
]