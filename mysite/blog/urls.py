from django.conf.urls import url, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^breakfast/$', views.breakfast, name='breakfast'),
    url(r'^dinner/$', views.dinner, name='dinner'),
    url(r'^snacks/$', views.snacks, name='snacks'),
    url(r'^about/$', views.about, name='about'),
    url(r'^recipe/(?P<pk>\d+)/$', views.fullrecipe, name='fullrecipe'),
    url(r'^recipe/(?P<pk>\d+)/like/$', views.fullrecipelike, name='fullrecipelike'),
    url(r'^recipe/new/$', views.new_recipe, name='new_recipe'),
    url(r'^recipe/(?P<pk>\d+)/edit/$', views.edit_recipe, name='edit_recipe'),
    url(r'^recipe/(?P<pk>\d+)/delete/$', views.delete_recipe, name='delete_recipe'),
    url(r'^register/$', views.registeruser, name='register'),
    url(r'^recipe/(?P<pk>\d+)/comment/$', views.add_comment, name='add_comment'),
    url(r'api/$', views.RecipeList.as_view()),
    url(r'api/top3likedrecipes/$', views.Top3LikedRecipes.as_view()),
    url(r'api/top3viewedrecipes/$', views.Top3ViewedRecipes.as_view()),
    url(r'api/mostlikedrecipe/$', views.MostLikedRecipe.as_view()),
    url(r'api/mostviewedrecipe/$', views.MostViewedRecipe.as_view()),
    url(r'api/breakfastlist/$', views.BreakfastList.as_view()),
    url(r'api/dinnerlist/$', views.DinnerList.as_view()),
    url(r'api/snackslist/$', views.SnackList.as_view()),
    url(r'^api/(?P<pk>\d+)/$', views.RecipeDetail.as_view()),
    url(r'^apidocs/', include('rest_framework_docs.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
