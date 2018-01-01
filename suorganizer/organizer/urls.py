from django.conf.urls import url
from . import views


urlpatterns =[
    url(r'tag/(?P<slug>[-\w]+)/$', views.tag_detail, name='organizer_tag_detail'),

]
