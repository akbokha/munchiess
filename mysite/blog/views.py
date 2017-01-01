from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import RecipeForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib.auth import login
from django.contrib.auth.models import User


def homepage(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    mostviewedposts = Post.objects.filter(published_date__lte=timezone.now()).order_by('views')
    mostlikedposts = Post.objects.filter(published_date__lte=timezone.now()).order_by('likes')
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
    return render(request, 'blog/recipe_edit.html', {'form': form})

@login_required
def edit_recipe(request, pk):
    recipe = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.published_date = timezone.now()
            recipe.save()
            return redirect('fullrecipe', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'blog/recipe_edit.html', {'form': form})

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
    posts = Post.objects.filter(published_date__lte=timezone.now(), category__icontains = "breakfast").order_by('published_date')
    return render(request, 'blog/breakfast.html', {'posts': posts})
    

    
