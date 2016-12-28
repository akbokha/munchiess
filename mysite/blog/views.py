from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

def homepage(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    mostviewedposts = Post.objects.filter(published_date__lte=timezone.now()).order_by('views')
    mostlikedposts = Post.objects.filter(published_date__lte=timezone.now()).order_by('likes')
    return render(request, 'blog/home.html', {'mostviewedposts': mostviewedposts, 'mostlikedposts': mostlikedposts
                                              ,'posts': posts})

def fullrecipe(request, pk):
    recipe = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/fullrecipe.html', {'recipe': recipe})
