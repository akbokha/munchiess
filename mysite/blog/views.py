from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import RecipeForm
from django.shortcuts import redirect

def homepage(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    mostviewedposts = Post.objects.filter(published_date__lte=timezone.now()).order_by('views')
    mostlikedposts = Post.objects.filter(published_date__lte=timezone.now()).order_by('likes')
    return render(request, 'blog/home.html', {'mostviewedposts': mostviewedposts, 'mostlikedposts': mostlikedposts
                                              ,'posts': posts})

def fullrecipe(request, pk):
    recipe = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/fullrecipe.html', {'recipe': recipe})

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


    
