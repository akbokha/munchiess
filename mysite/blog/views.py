from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import RecipeForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db.models import Max, Count
from rest_framework import generics
from .serializers import RecipeSerializer

def homepage(request):
    mostviewedposts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-views')[:3]
    mostlikedposts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-likes')[:3]
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/home.html', {'mostviewedposts': mostviewedposts, 'mostlikedposts': mostlikedposts
                                              ,'posts': posts})

def fullrecipe(request, pk):
    recipe = get_object_or_404(Post, pk=pk)
    recipe.increment_views()
    recipe.save()
    return render(request, 'blog/fullrecipe.html', {'recipe': recipe})

def fullrecipelike(request, pk):
    recipe = get_object_or_404(Post, pk=pk)
    recipe.increment_likes()
    recipe.save()
    return render(request, 'blog/fullrecipe.html', {'recipe': recipe})

@login_required
def new_recipe(request):
    edit = False
    if request.method == "POST":
        form = RecipeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.published_date = timezone.now()
            recipe.save()
            return redirect('fullrecipe', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'blog/recipe_edit.html', {'form': form, 'edit': edit})

@login_required
def edit_recipe(request, pk):
    edit = True
    recipe = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = RecipeForm(data=request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.published_date = timezone.now()
            if 'image' in request.FILES:
                recipe.image = request.FILES['image']
            recipe.save()
            return redirect('fullrecipe', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'blog/recipe_edit.html', {'form': form, 'edit': edit})


@login_required
def delete_recipe(request, pk):
    recipe = get_object_or_404(Post, pk=pk)
    recipe.delete()
    return redirect('homepage')

def registeruser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('homepage')
    else:
        form = UserForm()

    return render(request, 'registration/register.html', {'form': form})

def breakfast(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__icontains = "breakfast").order_by('-published_date')
    return render(request, 'blog/breakfast.html', {'posts': posts})

def dinner(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__icontains = "dinner").order_by('-published_date')
    return render(request, 'blog/dinner.html', {'posts': posts})

def snacks(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__icontains = "snacks").order_by('-published_date')
    return render(request, 'blog/snacks.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('fullrecipe', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/addcomment.html', {'form': form, 'recipe': post, 'pk': pk})

class RecipeList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = RecipeSerializer

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = RecipeSerializer

class Top3LikedRecipes(generics.ListCreateAPIView):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-likes')[:3]
    serializer_class = RecipeSerializer

class Top3ViewedRecipes(generics.ListCreateAPIView):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-views')[:3]
    serializer_class = RecipeSerializer

class MostLikedRecipe(generics.ListCreateAPIView):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-likes')[:1]
    serializer_class = RecipeSerializer

class MostViewedRecipe(generics.ListCreateAPIView):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-views')[:1]
    serializer_class = RecipeSerializer

class BreakfastList(generics.ListCreateAPIView):
    queryset = Post.objects.filter(published_date__lte=timezone.now(), category__icontains = "breakfast").order_by('-published_date')
    serializer_class = RecipeSerializer

class DinnerList(generics.ListCreateAPIView):
    queryset = Post.objects.filter(published_date__lte=timezone.now(), category__icontains = "dinner").order_by('-published_date')
    serializer_class = RecipeSerializer

class SnackList(generics.ListCreateAPIView):
    queryset = Post.objects.filter(published_date__lte=timezone.now(), category__icontains = "snacks").order_by('-published_date')
    serializer_class = RecipeSerializer
