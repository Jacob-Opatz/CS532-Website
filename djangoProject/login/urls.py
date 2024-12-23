# myapp/urls.py
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import register,process_text, custRegister

urlpatterns = [
    path('login/',views.customLogin.as_view(),name='login'),
    path('submit/', views.process_text, name='process_text'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', custRegister.as_view(), name='register'),
    # Built-in logout view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Built-in password reset views
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
