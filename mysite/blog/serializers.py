from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'text', 'created_date', 'image', 'views', 'likes', 'category')
