from django.conf.urls import url
from . import views


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
]
