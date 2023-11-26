from django.apps import apps
from django import forms
from .models import Contribution


Story = apps.get_model('storywriting', 'Story')

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'body', 'image', 'genre']
        
        
class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ['text']