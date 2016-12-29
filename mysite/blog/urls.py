from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^recipe/(?P<pk>\d+)/$', views.fullrecipe, name='fullrecipe'),
    url(r'^recipe/new/$', views.new_recipe, name='new_recipe'),
    url(r'^recipe/(?P<pk>\d+)/edit/$', views.edit_recipe, name='edit_recipe'),

]
