from django.conf.urls import url
from . import views



urlpatterns =[
    url(r'^startup/$', views.startup_list, name='organizer_startup_list'),
    url(r'^startup/(?P<slug>[-\w]+)/$', views.startup_detail, name='organizer_startup_detail'),
    url(r'^tag/$', views.tag_list, name='organizer_tag_list'),
    url(r'^tag/(?P<slug>[-\w]+)/$', views.tag_detail, name='organizer_tag_detail'),
]
