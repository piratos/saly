from django.contrib import admin
from tasks.models import ToDoTask, Project

class ToDoTaskAdmin(admin.ModelAdmin):
    def project__user(self, obj):
        return obj.project.user
    list_display = ('name', 'status', 'project', 'project__user')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'user')

admin.site.register(ToDoTask, ToDoTaskAdmin)
admin.site.register(Project, ProjectAdmin)
