from django.conf.urls import url
from . import views

app_name = 'organizer'

urlpatterns =[
    url(r'^tag/create/$', views.TagCreate.as_view(), name= 'organizer_tag_create'),
    url(r'^tag/$', views.tag_list, name='organizer_tag_list'),
    url(r'^tag/(?P<slug>[-\w]+)/$', views.tag_detail, name='organizer_tag_detail'),
    url(r'^startup/$', views.startup_list, name='organizer_startup_list'),
    url(r'^startup/(?P<slug>[-\w]+)/$', views.startup_detail, name='organizer_startup_detail'),


]
