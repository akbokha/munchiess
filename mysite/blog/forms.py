from django import forms
from django.contrib.auth.models import User
from .models import Post

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image', 'category')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
