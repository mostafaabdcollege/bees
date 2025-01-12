from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    
    path('', views.home, name='home'),
    
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('signup/', views.signup, name='signup'),
    
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.update_profile, name='update_profile'),
    path('chat/', views.chat_page, name='chat_page'),
    
]