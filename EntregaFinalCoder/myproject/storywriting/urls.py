from django.urls import path
from . import views

urlpatterns = [
    path('create_story/', views.create_story, name='create_story'),
    path('read_stories/', views.read_stories, name='read_stories'),
    path('join_story/<int:story_id>/', views.join_story, name='join_story'),
    path('browse_stories/', views.browse_stories, name='browse_stories'),
    path('story_detail/<int:story_id>/', views.story_detail, name='story_detail'),
]