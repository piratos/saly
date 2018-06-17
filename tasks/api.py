from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from tasks.models import Project, ToDoTask

## Serializers

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDoTask
        fields = ('name', 'status', 'priority', 'project')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'status', 'user')

## ViewSets
class TaskViewSet(viewsets.ModelViewSet):
    queryset = ToDoTask.objects.all()
    serializer_class = TaskSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

## Router
router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'projects', ProjectViewSet)
