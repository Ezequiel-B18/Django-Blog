from django import forms
from . import models

class CreatePost(forms.ModelForm):
    class Meta: #It must be named Meta
        model = models.Post
        fields = ["title", "body", "slug", "banner"]