from django.conf.urls import url
from . import views
from .feed import PostFeed

app_name='blog'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^single/(\d+)/$',views.single,name='single'),
    url(r'^category/(\d+)/$',views.category,name='category'),
    url(r'^tag/(\d+)/$',views.tag,name='tag'),
    url(r'archives/(\d+)/(\d+)/', views.archives, name='archives'),
    url(r'^rss/$', PostFeed(),name='rss'),
]