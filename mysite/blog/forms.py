from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image', 'category')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'comment',)
