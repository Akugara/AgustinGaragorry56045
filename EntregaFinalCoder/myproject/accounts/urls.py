from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.CustomLoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('create_story/', views.create_story, name='create_story'),
    path('login_redirect/', views.login_redirect, name='login_redirect'),
    path('edit_story/<int:story_id>/', views.edit_story, name='edit_story'),
    path('delete_story/<int:story_id>/', views.delete_story, name='delete_story'),
    
]