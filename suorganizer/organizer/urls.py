from django.conf.urls import url
from . import views

app_name = 'organizer'

urlpatterns =[
    url(r'^tag/create/$', views.TagCreate.as_view(), name= 'organizer_tag_create'),
    url(r'^tag/$', views.Taglist.as_view(), name='organizer_tag_list'),
    # url(r'^((?P<page_number>\d+))?$', views.TagPageList.as_view(), name='organizer_tag_page'),
    url(r'^tag/(?P<slug>[-\w]+)/$', views.tag_detail, name='organizer_tag_detail'),
    url(r'^tag/(?P<slug>[-\w]+)/update/$', views.TagUpdate.as_view(), name='organizer_tag_update'),
    url(r'^tag/(?P<slug>[-\w]+)/delete/$', views.TagDelete.as_view(), name='organizer_tag_delete'),
    url(r'^newslink/create/$', views.NewsLinkCreate.as_view(), name='organizer_newslink_create'),
    url(r'^newslink/update/(?P<pk>\d+)/$',views.NewsLinkUpdate.as_view(), name='organizer_newslink_update'),
    url(r'^newslink/delete/(?P<pk>\d+)/$',views.NewsLinkDelete.as_view(), name='organizer_newslink_delete'),
    url(r'^startup/$', views.StartupList.as_view(), name='organizer_startup_list'),
    url(r'^startup/create/$',views.StartupCreate.as_view(), name='organizer_startup_create'),
    url(r'^startup/(?P<slug>[-\w]+)/$', views.startup_detail, name='organizer_startup_detail'),
    url(r'^startup/(?P<slug>[-\w]+)/update/$', views.StartUpUpdate.as_view(), name='organizer_startup_update'),
    url(r'^startup/(?P<slug>[-\w]+)/delete/$', views.StartUpDelete.as_view(), name='organizer_startup_delete'),
]
