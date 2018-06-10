from django.conf.urls import url, include
from tasks import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addItem/(?P<taskname>.+)/$', views.add_task),
    url(r'^delItem/(?P<id>\d+)/$', views.remove_task),
    url(r'^status/(?P<id>\d+)/(?P<status>.+)/$', views.set_status),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]