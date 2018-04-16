from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^(?P<para>\w+)/$', views.param1, name='param1'),
    url(r'^(?P<para>\w+)/(?P<para2>\w+)/$', views.param2, name='param2'),
    url(r'^(?P<para>\w+)/(?P<para2>\w+)/(?P<para3>\w+)/$', views.param3, name='param3'),
    url(r'^(?P<para>\w+)/(?P<para2>\w+)/(?P<para3>\w+)/(?P<para4>\w+)', views.param4, name='param4'),
]