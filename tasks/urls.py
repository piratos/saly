from django.conf.urls import url, include
from tasks import views

urlpatterns = [
    url(r'$', views.index),
]