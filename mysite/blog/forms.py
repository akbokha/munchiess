from django import forms

from .models import Post

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image', 'category')
