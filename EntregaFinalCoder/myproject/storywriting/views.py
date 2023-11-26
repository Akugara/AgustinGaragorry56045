from django.shortcuts import render, redirect
from .forms import StoryForm
from .models import Story
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Story, Contribution
from .forms import ContributionForm
from django.db.models import Q

# Función para crear una historia
# Crea un form para crear una historia, y si es válido, se guarda y te redirige a la página de leer historias
@login_required
def create_story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            story = form.save(commit=False)
            story.user = request.user
            story.save()
            # messages.success(request, 'You have successfully created a story.')
            return redirect('read_stories')
    else:
        form = StoryForm()
    context = {'form': form}
    return render(request, 'storywriting/create_story.html', context)


# Función para leer historias
# Obtiene todas las historias y las ordena por fecha de creación
def read_stories(request):
    stories = Story.objects.all().order_by('-created_at')
    context = {'stories': stories}
    return render(request, 'storywriting/read_stories.html', context)


# Función para editar una historia
# Obtiene la historia que se quiere editar y si el usuario es el creador de la historia, se edita
@login_required(login_url='login_redirect')
def join_story(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    if request.method == 'POST':
        form = ContributionForm(request.POST)
        if form.is_valid():
            contribution = form.save(commit=False)
            contribution.story = story
            contribution.user = request.user
            contribution.save()
            # Actualiza el cuerpo de la historia con la contribución
            story.body += "\n" + contribution.text
            story.save()
            return redirect('story_detail', story_id=story.id)
    else:
        form = ContributionForm()
    return render(request, 'storywriting/join_story.html', {'story': story, 'form': form})

# Función para editar una historia
# Obtiene la historia que se quiere editar y si el usuario es el creador de la historia le permite editar el original
def story_detail(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    return render(request, 'storywriting/story_detail.html', {'story': story})

# Función para retornar todas las historias de la database y filtrarlas por título, usuario o género
def browse_stories(request):
    stories = Story.objects.all()
    return render(request, 'storywriting/browse_stories.html', {'stories': stories})


def browse_stories(request):
    query = request.GET.get('q')
    if query:
        stories = Story.objects.filter(
            Q(title__icontains=query) |
            Q(user__username__icontains=query) |  
            Q(genre__icontains=query)
        )
    else:
        stories = Story.objects.all()

    return render(request, 'storywriting/browse_stories.html', {'stories': stories})