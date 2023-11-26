
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.shortcuts import get_object_or_404
from storywriting.forms import StoryForm
from django.apps import apps

Story = apps.get_model('storywriting', 'Story')


class CustomLoginView(auth_views.LoginView):
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

def login_redirect(request):
    return redirect('login')

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile(request):
    user_stories = Story.objects.filter(user=request.user)
    return render(request, 'accounts/profile.html', {'stories': user_stories})

@login_required
def edit_story(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES, instance=story)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Story updated successfully')
            return redirect('profile')
    else:
        form = StoryForm(instance=story)
    return render(request, 'accounts/edit_story.html', {'form': form})

@login_required
def delete_story(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    if request.user == story.user:
        story.delete()
        # messages.success(request, 'Story deleted successfully')
    return redirect('profile')



@login_required(login_url='login_redirect')
def create_story(request):
    return render(request, 'accounts/create_story.html')

