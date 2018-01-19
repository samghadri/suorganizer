from django.conf.urls import url
from . import views

# app_name = 'blog'

urlpatterns=[
    url(r'^$', views.PostList.as_view(), name='blog_post_list'),
    url(r'^create/$', views.PostCreate.as_view(), name='blog_post_create'),
    url(r'^(?P<year>\d{4})/'
        r'(?P<month>\d{1,2})/'
        r'(?P<slug>[-\w]+)/$',
        views.post_detail, name='blog_post_detail'),
    url(r'^(?P<year>\d{4})/'
        r'(?P<month>\d{1,2})/'
        r'(?P<slug>[\w\-]+)/'
        r'update/$', views.PostUpdate.as_view(), name='blog_post_update'),

]
