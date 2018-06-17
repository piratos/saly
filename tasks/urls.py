from django.conf.urls import url, include
from tasks import views
from django.conf.urls import url, include
from tasks.api import router

urlpatterns = [
    url(r'^$', views.index),
    url(r'^api/', include(router.urls)),
    url(r'^addItem/(?P<taskname>.+)/$', views.add_task),
    url(r'^delItem/(?P<id>\d+)/$', views.remove_task),
    url(r'^status/(?P<id>\d+)/(?P<status>.+)/$', views.set_status),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^api_auth/', include('rest_framework.urls')),
]
